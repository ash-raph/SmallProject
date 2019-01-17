from django.views.generic import ListView
from shops.models import Shops


class ShopsListView(ListView):
    model = Shops
    template_name = 'shops_list.html'
