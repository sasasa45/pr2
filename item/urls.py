from django.urls import path
from .views import *
from django.conf.urls import include

urlpatterns = [
    path('', ItemsIndex.as_view(),name='index'),
    path('category/<str:slug>/', CategoriesDetail.as_view(),name='category'),
    path('search/', ItemsSearch.as_view(),name='search'),
    path('products/<int:pk>', ItemDetail.as_view(),name='itemdetail'),
    path('like/<int:pk>', like ,name='like'),
    path('unlike/<int:pk>', unlike ,name='unlike'),
    path('addcart/<int:pk>', add_to_cart ,name='addtocart'),
    path('likes/', LikeView.as_view(),name='likes'),
    path('api/', include(("item.api.urls",'item-api'), namespace='item_api')),


]
