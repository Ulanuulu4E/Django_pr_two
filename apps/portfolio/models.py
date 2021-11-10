from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(
        verbose_name = "название", 
        max_length=120
    )


    description = models.TextField(
        verbose_name = "описание"
    )

    image = models.ImageField(
        upload_to='portfolio',
        verbose_name='Картинки',
        blank=True, null=True
    )

    link_portfolio = models.CharField(max_length=220, verbose_name='Ссылка на партфолио')



    def __str__(self):
      return self.title

class Meta:
     verbose_name_plural = 'Портфолио'