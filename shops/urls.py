from django.conf.urls import url
from shops.views import ShopsListView

urlpatterns = [
    url(r'^shops/', ShopsListView.as_view(), name="list_of_shops"),
]
