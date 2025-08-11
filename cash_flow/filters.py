import django_filters

from cash_flow.models import CashFlow


class CashFlowFilter(django_filters.FilterSet):
    """Фильтрация для CashFlowListView"""
    class Meta:
        model = CashFlow
        fields = ('date_was_created', 'status', 'type', 'category', 'subcategory')