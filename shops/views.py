from django.views.generic import ListView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.shortcuts import reverse
from shops.models import Shop, ShopUser
from django.utils.timezone import now


class ShopsListView(ListView):
    model = Shop
    template_name = 'shops_list.html'

    def get_queryset(self):
        return super().get_queryset().order_by('distance')

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
