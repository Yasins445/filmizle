# Generated by Django 5.0.1 on 2024-02-05 17:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmApp', '0005_remove_film_slug_alter_kategori_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kategori',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
