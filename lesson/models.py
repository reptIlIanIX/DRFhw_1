from django.db import models

from DRFhw_1 import settings


class Lesson(models.Model):
    name = models.CharField(max_length=40, verbose_name='name')
    description = models.TextField(verbose_name='description')
    image = models.ImageField(verbose_name='image', null=True)
    link = models.URLField(verbose_name='link', null=True)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=4)

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Урок'

    def __str__(self):
        return self.name
