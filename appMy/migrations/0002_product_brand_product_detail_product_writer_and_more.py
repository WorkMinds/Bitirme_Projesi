# Generated by Django 4.1.5 on 2023-04-05 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50, verbose_name='Yayınevi'),
        ),
        migrations.AddField(
            model_name='product',
            name='detail',
            field=models.TextField(blank=True, verbose_name='Özellikler'),
        ),
        migrations.AddField(
            model_name='product',
            name='writer',
            field=models.CharField(blank=True, max_length=50, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, verbose_name='Slug Kategori'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Fotoğraf'),
        ),
    ]
