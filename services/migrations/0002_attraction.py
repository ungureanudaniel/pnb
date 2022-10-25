# Generated by Django 4.1.2 on 2022-10-25 09:06

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WebP', keep_meta=True, quality=75, scale=0.5, size=[640, None], upload_to='attraction_images')),
                ('text', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField()),
                ('categ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.attractioncategory')),
            ],
        ),
    ]