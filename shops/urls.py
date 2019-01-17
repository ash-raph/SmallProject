from django.conf.urls import url
from shops.views import ShopsListView, ReactView

urlpatterns = [
    url(r'^shops/$', ShopsListView.as_view(), name="list_of_shops"),
    url(r'^shops/(?P<pk>\d+)/react/$', ReactView.as_view(), name="like_dislike"),
]
