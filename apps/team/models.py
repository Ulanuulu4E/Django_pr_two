from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(
        verbose_name = "Имя", 
        max_length=120
    )

    last_name = models.CharField(
        verbose_name = "Фамиля", 
        max_length=120
    )


    logo = models.ImageField(
        upload_to='banner',
        verbose_name='logo',
        blank=True, null=True
    )

    zvaniya = models.CharField(verbose_name="звание",max_length=225)
    description = models.CharField(max_length=225, verbose_name='Описание')
    age = models.CharField(max_length=32, verbose_name='возраст')
    Department = models.CharField(max_length=225, verbose_name='оделение')
    Experience = models.CharField(max_length=225, verbose_name='опыт')
    Phone = models.CharField(max_length=22, verbose_name='телефон')
    email = models.CharField(max_length=225, verbose_name='email')
    address = models.CharField(max_length=225, verbose_name='Address')
    Facebook = models.CharField(max_length=225, verbose_name='Facebook')
    Telegram = models.CharField(max_length=225, verbose_name='Telegram')
    Twitter = models.CharField(max_length=225, verbose_name='Twitter')
    Instagram = models.CharField(max_length=225, verbose_name='Instagram')


    def __str__(self):
      return self.title

class Meta:
     verbose_name_plural = 'Команда'