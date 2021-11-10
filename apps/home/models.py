from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        verbose_name = "название", 
        max_length=120
    )


    logo = models.ImageField(
        upload_to='banner',
        verbose_name='logo',
        blank=True, null=True
    )

    keyword = models.CharField(verbose_name="Ключевые слова",max_length=225)
    phone = models.CharField(max_length=20, verbose_name='телефон')
    time_work = models.CharField(max_length=225, verbose_name='время работы')
    day_work = models.CharField(max_length=225, verbose_name='дни работы')
    email = models.CharField(max_length=225, verbose_name='email')
    address = models.CharField(max_length=225, verbose_name='Address')
    Facebook = models.CharField(max_length=225, verbose_name='Facebook')
    Telegram = models.CharField(max_length=225, verbose_name='Telegram')
    Twitter = models.CharField(max_length=225, verbose_name='Twitter')
    Instagram = models.CharField(max_length=225, verbose_name='Instagram')


    def __str__(self):
      return self.title

class Meta:
     verbose_name_plural = 'Основные настройки'