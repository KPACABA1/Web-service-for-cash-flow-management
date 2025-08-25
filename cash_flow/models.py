from django.db import models
from django.utils import timezone


class Category(models.Model):
    """Модель категории"""
    name = models.CharField(max_length=20, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    """Модель подкатегории"""
    name = models.CharField(max_length=20, verbose_name='Название', unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategory_category')

    def __str__(self):
        return self.name


class Type(models.Model):
    """Модель типа"""
    name = models.CharField(max_length=20, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    """Модель статуса"""
    name = models.CharField(max_length=20, verbose_name='Название', unique=True)

    def __str__(self):
        return self.name


class CashFlow(models.Model):
    """Модель движения денежных средств."""
    date_was_created = models.DateField(default=timezone.now, verbose_name='Дата создания')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, related_name='cashflow_status',
                             verbose_name='Статус')
    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, related_name='cashflow_type',
                             verbose_name='Тип')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='cashflow_category',
                                 verbose_name='Категория')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True,
                                    related_name="cashflow_subcategory", verbose_name='Подкатегория')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    class Meta:
        verbose_name = 'Движение денежных средств'
        verbose_name_plural = 'Движения денежных средств'

    def __str__(self):
        return f'{self.category}, {self.subcategory} - {self.type}'
