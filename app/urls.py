from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('category/', views.category, name="category"),
    path('search/', views.search, name="search"),
    path('logout/', views.logoutPage, name="logout"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item', views.updateItem, name='update_item'),
    path('detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('introduce/', views.introduce, name='introduce')
]
# home là hàm trong view