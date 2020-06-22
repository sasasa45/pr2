from django.urls import path, include
from .views import ItemsViewSet
from rest_framework import routers
name_app='item-api'
# router=routers.DefaultRouter()
# router.register('items',ItemsViewSet, basename='items')
urlpatterns=[
        # path('', include(router.urls)),
        path('',ItemsViewSet.as_view({'get': 'list'}),name='list'),
]
