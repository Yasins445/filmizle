# Generated by Django 5.0.1 on 2024-02-05 19:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmApp', '0006_alter_kategori_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='film_adi', unique=True),
        ),
    ]
