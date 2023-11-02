from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='name')
    surname = models.CharField(max_length=50, verbose_name='surname')
    email = models.EmailField(max_length=50, verbose_name='email', null=True, blank=True)
    phone = models.IntegerField(verbose_name='phone', null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name='city')
    image = models.ImageField(verbose_name='image', null=True, blank=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.name} {self.surname}"
