from django.db import models

PAY_CARD = 'card'
PAY_CASH = 'cash'


PAY_TYPES = (
        (PAY_CASH, 'наличные'),
        (PAY_CARD, 'перевод')
    )


class Payment(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    payday = models.DateField(verbose_name='payday')
    lesson = models.ForeignKey('lesson.Lesson', on_delete=models.CASCADE)
    amount = models.IntegerField(verbose_name='amount')
    method = models.CharField(choices=PAY_TYPES, default=PAY_CASH)