from django.urls import path
from cash_flow.apps import CashFlowConfig
from cash_flow.views import CashFlowListView, TypeCreateView, StatusCreateView, CategoryCreateView, \
    SubcategoryCreateView, CashFlowCreateView, load_subcategories

app_name = CashFlowConfig.name

urlpatterns = [
    # Урлы для движения денежных средств
    path('', CashFlowListView.as_view(), name='cash_flow-list'),
    path('cash_flow_create', CashFlowCreateView.as_view(), name='cash_flow-create'),
    path('ajax/load-subcategories/', load_subcategories, name='load_subcategories'),

    # Урлы для типов движения денежных средств
    path('type_create', TypeCreateView.as_view(), name='type-create'),

    # Урлы для статусов движения денежных средств
    path('status_create', StatusCreateView.as_view(), name='status-create'),

    # Урлы для категорий движения денежных средств
    path('category_create', CategoryCreateView.as_view(), name='category-create'),

    # Урлы для подкатегорий движения денежных средств
    path('subcategory_create', SubcategoryCreateView.as_view(), name='subcategory-create'),
]
