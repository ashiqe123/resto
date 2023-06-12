from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name='index'),
    path('cat',views.cat,name='cat'),
    path('about',views.about,name='about'),
     path('cart',views.cart,name='cart'),
     path('lg',views.lg,name='lg'),
    path('home',views.home,name='home'),
]