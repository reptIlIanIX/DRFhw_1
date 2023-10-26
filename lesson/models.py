from django.db import models


class Lesson(models.Model):
    name = models.CharField(max_length=40, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='image', null=True)
    link = models.URLField(verbose_name='link', null=True)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Урок'

    def __str__(self):
        return self.name
