from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.utils.timezone import now, timedelta
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from shops.forms import CreationUserForm
from django.shortcuts import reverse

from shops.models import Shop, ShopUser


class ShopsListView(LoginRequiredMixin, ListView):
    model = Shop
    template_name = 'shops_list.html'

    def get_queryset(self):
        disliked = list(ShopUser.objects.filter(disliked_at__gt=now() - timedelta(hours=2))
                        .values_list("shop__id", flat=True))
        liked = list(self.request.user.liked_shops.values_list('id', flat=True))

        return super().get_queryset()\
            .exclude(pk__in=liked + disliked)\
            .order_by('distance')

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx.update({'main': True})
        return ctx


class LikeShopView(LoginRequiredMixin, View):
    model = ShopUser

    def get_success_url(self):
        return reverse('list_of_shops')

    def post(self, *args, **kwargs):
        self.request.user.liked_shops.add(kwargs.get('shop'))
        return HttpResponseRedirect(self.get_success_url())


class RemoveShopView(LoginRequiredMixin, View):
    model = ShopUser

    def get_success_url(self):
        return reverse("list_of_liked_shops")

    def post(self, *args, **kwargs):
        self.request.user.liked_shops.remove(kwargs.get('shop'))
        return HttpResponseRedirect(self.get_success_url())


class LikedShopsListView(LoginRequiredMixin, ListView):
    template_name = 'shops_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super().get_context_data(object_list=object_list, **kwargs)
        ctx.update({'main': False})
        return ctx

    def get_queryset(self):
        return self.request.user.liked_shops.all()


class DislikeShopView(LoginRequiredMixin, View):
    def get_success_url(self):
        return reverse('list_of_shops')

    def get_object(self):
        return ShopUser.objects.get_or_create(user_id=self.request.user.pk, shop_id=self.kwargs.get('shop'))[0]

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.disliked_at = now()
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


class CreateUserView(CreateView):
    form_class = CreationUserForm
    template_name = 'create_user.html'
#    success_url = reverse('list_of_shops')

    def get_success_url(self):
        return reverse('list_of_shops')


