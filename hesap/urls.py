from django.urls import path
from . import views

urlpatterns = [
    path("giris", views.giris_request, name="giris"),
    path("kaydol", views.kaydol_request, name="kaydol"),
    path("cik", views.cik_request, name="cik"),
]
