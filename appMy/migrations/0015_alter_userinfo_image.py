# Generated by Django 4.1.5 on 2023-04-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0014_alter_userinfo_image_alter_userinfo_job_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.FileField(default='media/None/default.png', upload_to=None, verbose_name='Resim'),
        ),
    ]
