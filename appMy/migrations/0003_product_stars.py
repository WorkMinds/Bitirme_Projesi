# Generated by Django 4.1.5 on 2023-04-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0002_product_brand_product_detail_product_writer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stars',
            field=models.FloatField(default=0, verbose_name='Puan'),
        ),
    ]
