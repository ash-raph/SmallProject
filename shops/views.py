from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from shops.models import Shop, ShopUser
from django.utils.timezone import now, timedelta
from django.shortcuts import reverse


class ShopsListView(ListView):
    model = Shop
    template_name = 'shops_list.html'

    def get_queryset(self):
        disliked = list(ShopUser.objects.filter(disliked_at__gt=now() + timedelta(hours=2))
                        .values_list("shop__id", flat=True))
        liked = list(self.request.user.shops.values_list('id', flat=True))

        return super().get_queryset()\
            .exclude(pk__in=liked + disliked)\
            .order_by('distance')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx.update({'main': True})
        return ctx


class LikeShopView(View):
    model = ShopUser

    def get_success_url(self):
        return reverse('list_of_shops')

    def post(self, *args, **kwargs):
        ShopUser(user=self.request.user, shop=Shop.objects.get(pk=kwargs.get('shop'))).save()
        return HttpResponseRedirect(self.get_success_url())


class RemoveShopView(DeleteView):
    model = ShopUser

    def get_success_url(self):
        return reverse("list_of_liked_shops")

    def get_object(self, queryset=None):
        return ShopUser.objects.get(user=self.request.user, shop__id=self.kwargs.get('shop'))


class LikedShopsListView(ListView):
    template_name = 'shops_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx.update({'main': False})
        return ctx

    def get_queryset(self):
        return self.request.user.shops.all()


class DislikeShopView(View):
    def get_success_url(self):
        return reverse('list_of_shops')

    def get_object(self):
        return ShopUser.objects.get(user=self.request.user, shop__id=self.kwargs.get('shop'))

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.disliked_at = now()
        obj.save()
        return HttpResponseRedirect(self.get_success_url())
