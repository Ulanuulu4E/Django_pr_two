# Generated by Django 3.2.9 on 2021-11-10 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='Facebook',
            field=models.CharField(max_length=225, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='day_work',
            field=models.CharField(max_length=225, verbose_name='дни работы'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='телефон'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='time_work',
            field=models.CharField(max_length=225, verbose_name='время работы'),
        ),
    ]