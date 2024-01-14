from django.db import models

from DRFhw_1 import settings
from course.models import Course


# Create your models here.
class Subscription (models.Model):
    is_active = models.BooleanField(default=True, verbose_name='активна')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс', blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True )

    def __str__(self):
        return f'{self.user}: {self.course} {self.is_active}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
        unique_combine = ('user', 'course')
