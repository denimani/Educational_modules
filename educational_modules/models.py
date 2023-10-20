from django.db import models

from users.models import User

NULLABLE = {
    'null': True,
    'blank': True,
}


class EducationalModule(models.Model):
    """
    Модель образовательного модуля
    """
    name = models.CharField(max_length=255, verbose_name='Название')
    order_number = models.IntegerField(unique=True, verbose_name='Порядковый номер')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    user = models.ManyToManyField(User, verbose_name='Создатель модуля', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Образовательный модуль'
        verbose_name_plural = 'Образовательные модули'
