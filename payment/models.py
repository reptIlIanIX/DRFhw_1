from datetime import datetime

from django.db import models

PAY_CARD = 'card'
PAY_CASH = 'cash'

PAY_TYPES = (
    (PAY_CASH, 'наличные'),
    (PAY_CARD, 'перевод')
)


class Payment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    payday = models.DateField(verbose_name='payday', blank=True, null=True)
    lesson = models.ForeignKey('lesson.Lesson', on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(verbose_name='amount')
    method = models.CharField(max_length=200, choices=PAY_TYPES, default=PAY_CASH, verbose_name='method')
