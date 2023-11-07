from django.db import models

from DRFhw_1 import settings


class Course(models.Model):
    name = models.CharField(max_length=40, verbose_name='name')
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    description = models.TextField(verbose_name='description', null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=3)

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name
