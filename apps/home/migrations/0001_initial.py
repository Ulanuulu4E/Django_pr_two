# Generated by Django 3.2.9 on 2021-11-09 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='название')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='banner', verbose_name='logo')),
                ('keyword', models.CharField(max_length=225, verbose_name='Ключевые слова')),
                ('phone', models.CharField(max_length=20, verbose_name='phone')),
                ('time_work', models.CharField(max_length=225, verbose_name='time_work')),
                ('day_work', models.CharField(max_length=225, verbose_name='day_work')),
                ('email', models.CharField(max_length=225, verbose_name='email')),
                ('address', models.CharField(max_length=225, verbose_name='Address')),
                ('Facebook', models.CharField(max_length=225, verbose_name='Faceboo')),
                ('Telegram', models.CharField(max_length=225, verbose_name='Telegram')),
                ('Twitter', models.CharField(max_length=225, verbose_name='Twitter')),
                ('Instagram', models.CharField(max_length=225, verbose_name='Instagram')),
            ],
        ),
    ]