from django.db import models

# Create your models here.
class Price(models.Model):
    title = models.CharField(
        verbose_name = "название", 
        max_length=120
    )

    price = models.CharField(max_length=225, verbose_name='цена')
    Per_Month = models.CharField(max_length=225, verbose_name='в месяц')

    description = models.CharField(
        verbose_name = "описание", 
        max_length=120
    )



    def __str__(self):
      return self.title

class Meta:
     verbose_name_plural = 'Цены'