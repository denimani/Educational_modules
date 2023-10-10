from django.db import models

# NULLABLE = {
#     'null': True,
#     'blank': True,
# }
#
#
# class EducationalModule(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название')
#     order_number = models.IntegerField(verbose_name='Порядковый номер')
#     description = models.TextField(verbose_name='Описание')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Образовательный модуль'
#         verbose_name_plural = 'Образовательные модули'
#