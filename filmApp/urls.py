from django.urls import path
from .views import*
from . import views

urlpatterns = [
    path('',index,name='anasayfa'),
    path('home',views.index,name='index'),
    path('film',views.film, name='film'),
    path('film/<slug:slug>',views.filmdetay, name='filmdetay'),
    path("kategori/<slug:slug>", views.filmler_by_kategori, name="filmler_by_kategori"),

]