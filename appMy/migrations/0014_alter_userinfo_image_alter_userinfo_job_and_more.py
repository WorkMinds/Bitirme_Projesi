# Generated by Django 4.1.5 on 2023-04-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0013_alter_userinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='image',
            field=models.FileField(default='media/None/team-member5.jpg', upload_to=None, verbose_name='Resim'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='job',
            field=models.CharField(default='-', max_length=50, verbose_name='İş'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.CharField(default='-', max_length=50, verbose_name='Telefon Numarası'),
        ),
    ]
