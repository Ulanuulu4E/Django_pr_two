from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(
        verbose_name = "название", 
        max_length=120
    )


    description = models.TextField(
        verbose_name = "описание"
    )

    image = models.ImageField(
        upload_to='news',
        verbose_name='Картинки',
        blank=True, null=True
    )

    date = models.DateField(auto_now_add=True)


    def __str__(self):
      return self.title

class Meta:
     verbose_name_plural = 'Новости'