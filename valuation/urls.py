from django.urls import path, include
from .views import *

urlpatterns = [
    path('products/<int:pk>/rate_comment/', RateComment.as_view(),name='ratecomment'),



]
