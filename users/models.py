from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class UserRoles(models.TextChoices):
    """
            Класс перечисления для определения ролей пользователя.

            Attributes:
                MEMBER (str): Значение роли 'member'.
                MODERATOR (str): Значение роли 'moderator'.
        """
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')



class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True, verbose_name='name')
    surname = models.CharField(max_length=50, verbose_name='surname')
    email = models.EmailField(max_length=50, verbose_name='email', null=True, blank=True)
    phone = models.IntegerField(verbose_name='phone', null=True, blank=True)
    city = models.CharField(max_length=30, verbose_name='city')
    image = models.ImageField(verbose_name='image', null=True, blank=True)
    role = models.CharField(max_length=11, choices=UserRoles.choices, default=UserRoles.MEMBER)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.username} {self.surname}"
