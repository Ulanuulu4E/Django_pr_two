from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(
        verbose_name = "название", 
        max_length=120
    )


    logo = models.ImageField(
        upload_to='banner',
        verbose_name='logo',
        blank=True, null=True
    )

    description = models.CharField(
        verbose_name = "описание", 
        max_length=225
    )


    def __str__(self):
      return self.title

class Meta:
     verbose_name_plural = 'Детали обслуживания'