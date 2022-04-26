from django.db import models
from django.utils import timezone
from django.conf import settings


class RandomInt(models.Model):
    random_number = models.SmallIntegerField(verbose_name='Случайное число')
    created = models.DateField(blank=True, null=True, default=timezone.now, verbose_name='Дата создания записи')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Случайное число'
        verbose_name_plural = 'Случайные числа'