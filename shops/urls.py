# shops/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShopListView, name='shop-list'),
    path('register_shop/', views.register_shop, name='register_shop'),

    # path('register_shop', views.ShopListView, name='shop-list'),

    # Add other shop-related URLs as needed
]
