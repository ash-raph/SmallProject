from django.views.generic import ListView
from django.views.generic.base import View
from django.shortcuts import redirect, reverse
from shops.models import Shops


class ShopsListView(ListView):
    model = Shops
    template_name = 'shops_list.html'


class ReactView(View):
    def post(self, request, **kwargs):
        shop_instance = Shops.objects.filter(pk=kwargs.get('pk')).first()

        if 'Like' in request.POST:
            self.request.user.shops.add(shop_instance)

        elif 'Dislike' in request.POST:
            self.request.user.shops.remove(shop_instance)

        return redirect(reverse('list_of_shops'))
