# Generated by Django 4.1.2 on 2022-10-19 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttractionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Attraction Category',
                'verbose_name_plural': 'Attraction Categories',
            },
        ),
    ]
