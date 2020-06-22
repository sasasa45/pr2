from django.urls import path, include
from .views import *

urlpatterns = [
    path('cart/', Cart.as_view(),name='cart'),
    path('refresh/', Refresh.as_view(),name='refresh'),
    path('delete_item_cart/<int:pk>/', DeleteItemCart.as_view(),name='delete_item_cart'),
    path('checkout/', CheckoutView.as_view(),name='checkout'),
    path('promocode/', Promocode.as_view(),name='promocode'),
    path('order_list/', OrderList.as_view(),name='order'),
    path('order/<int:pk>/', OrderDetail.as_view(),name='orderdetail'),
    path('order/<int:pk>/comment/', OrderCommentView.as_view(),name='ordercomment'),
    path('staff_order_list/', StaffOrderView.as_view(),name='staff_order'),
    path('staff_order_list/<int:pk>/', OrderUpdate.as_view(),name='staff_order_update'),
]
