# Generated by Django 5.0.1 on 2024-02-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmApp', '0002_alter_film_resim_alter_film_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]