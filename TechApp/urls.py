from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.user_login, name='login'),
    path('product', views.product_list, name='product'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.view_cart, name='view_cart'),
    path('remove/<int:product_id>/', views.removecart, name='removecart'),
]