from django.contrib import admin
from .models import Kategori,Film
from django.utils.safestring import mark_safe
# Register your models here.

class Filmadmin(admin.ModelAdmin):
    list_display = ["film_adi","anasayfa_goster","slug","secilen_kategori"]
    list_editable = ["anasayfa_goster"]
    search_fields = ["film_adi","aciklama"]
    readonly_fields = ["slug"]
    list_filter = ["anasayfa_goster", "kategori"]

    def secilen_kategori(self,obje):
        html = "<ul>"

        for kategori in obje.kategori.all():
            html += "<li>" + kategori.name + "</li>"

        html += "</ul>"
        return mark_safe(html)



admin.site.register(Kategori)
admin.site.register(Film,Filmadmin)