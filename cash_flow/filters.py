import django_filters
from django import forms

from cash_flow.models import CashFlow, Status, Type, Category, Subcategory


class CashFlowFilter(django_filters.FilterSet):
    """Фильтрация для CashFlowListView"""
    # Существующие фильтры
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        empty_label="Все статусы"
    )
    type = django_filters.ModelChoiceFilter(
        queryset=Type.objects.all(),
        empty_label="Все типы"
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        empty_label="Все категории"
    )
    subcategory = django_filters.ModelChoiceFilter(
        queryset=Subcategory.objects.all(),
        empty_label="Все подкатегории"
    )

    # Новые фильтры для даты
    start_date = django_filters.DateFilter(
        field_name='date_was_created',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата с'
    )

    end_date = django_filters.DateFilter(
        field_name='date_was_created',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата по'
    )

    class Meta:
        model = CashFlow
        fields = ('status', 'type', 'category', 'subcategory')