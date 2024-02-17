from django.shortcuts import render
from .models import Kategori,Film
# Create your views here.

def index(request):
 data = {
    "kategoriler":Kategori.objects.all(),
    "filmler":Film.objects.filter(anasayfa_goster = True)
 }

 return render(request,'index.html', data)


def film(request):
    data = {
    "kategoriler":Kategori.objects.all(),
    "filmler":Film.objects.all()
 }
    return render(request,'film.html', data)

def filmdetay(request,slug):
   data = {
      "film":Film.objects.get(slug=slug)
   }
   return render(request,'filmdetay.html',data)
   



def filmler_by_kategori(request, slug):
    data = {
    "kategoriler":Kategori.objects.all(),
    "filmler":Film.objects.filter(kategori__slug=slug),
    "secilen_film": slug
 }
    return render(request,"film.html",data)