from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name='index'),
    path('cat',views.cat,name='cat'),
    path('about',views.about,name='about'),
     path('cart',views.cart,name='cart'),
     path('lg',views.lg,name='lg'),
    path('home',views.home,name='home'),
    path('wl',views.wl,name='wl'),
    path('catlog',views.catlog,name='catlog'),
    path('logcart',views.logcart,name='logcart'),
    path('wl2',views.wl2,name='wl2'),
]