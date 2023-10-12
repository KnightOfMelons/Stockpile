from django.db import models


class Roll(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, verbose_name='ID')
    length = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Длина (м)')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес (кг)')
    date_added = models.DateTimeField(verbose_name='Даба добавления')
    # МОЖНО СДЕЛАТЬ, ЧТОБЫ ОНА СРАЗУ ЗАПОЛНЯЛАСЬ ДАТОЙ И ВРЕМЕНЕМ, КОТОРЫЕ СЕГОДНЯ, НО Я НЕ СТАЛ, А ТАК
    # date_added = models.DateTimeField(auto_now_add=True)
    date_removed = models.DateTimeField(null=True, blank=True, verbose_name='Даба удаления')

    class Meta:
        ordering = ['pk']
        verbose_name = u"Рулон"
        verbose_name_plural = u"Рулоны"

    def __str__(self):
        return f'Номер {self.id} | Длина {self.length} | Вес {self.weight}'
