from django.db import models
from django.utils.text import slugify
from autoslug import AutoSlugField
# Create your models here.

class Kategori(models.Model):
    name = models.CharField(max_length =200)
    slug = AutoSlugField(null =True, unique =True , default=None , populate_from='name')

    def __str__(self):
        return self.name

                                            
class Film(models.Model):
    film_adi = models.CharField(max_length = 200)
    aciklama = models.TextField()
    resim = models.ImageField( upload_to= 'film-img/')
    video = models.FileField( upload_to='film-video/')
    kategori = models.ManyToManyField(Kategori)
    anasayfa_goster = models.BooleanField( default = False)
    slug = AutoSlugField(null =True, unique =True , default=None , populate_from='film_adi')
   

    

    def __str__(self):
        return self.film_adi