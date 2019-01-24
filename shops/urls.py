from django.conf.urls import url
from shops.views import ShopsListView, LikedShopsListView, LikeShopView, RemoveShopView, \
    DislikeShopView, CreateUserView

urlpatterns = [
    # default view is shops list
    url(r'^$', ShopsListView.as_view()),

    url(r'^shops/$', ShopsListView.as_view(), name="list_of_shops"),
    url(r'^shops/liked/$', LikedShopsListView.as_view(), name="list_of_liked_shops"),
    url(r'^shops/(?P<shop>\d+)/like/$', LikeShopView.as_view(), name="like_shop"),
    url(r'^shops/(?P<shop>\d+)/remove/$', RemoveShopView.as_view(), name="remove_shop"),
    url(r'^shops/(?P<shop>\d+)/dislike/$', DislikeShopView.as_view(), name="dislike_shop"),
    url(r'^accounts/user/$', CreateUserView.as_view(), name="create_user"),
]
