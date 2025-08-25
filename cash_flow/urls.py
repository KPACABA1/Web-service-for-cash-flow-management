from django.urls import path
from cash_flow.apps import CashFlowConfig
from cash_flow.views import CashFlowListView, TypeCreateView, StatusCreateView, CategoryCreateView, \
    SubcategoryCreateView, CashFlowCreateView, load_subcategories, CashFlowUpdateView, CashFlowDeleteView, \
    TypeUpdateView, TypeDeleteView, StatusUpdateView, StatusDeleteView, CategoryUpdateView, CategoryDeleteView, \
    SubcategoryUpdateView, SubcategoryDeleteView

app_name = CashFlowConfig.name



urlpatterns = [
    # Урлы для движения денежных средств
    path('', CashFlowListView.as_view(), name='cash_flow-list'),
    path('cash_flow_create/', CashFlowCreateView.as_view(), name='cash_flow-create'),
    path('ajax/load-subcategories/', load_subcategories, name='load_subcategories'),
    path('cash_flow_update/<int:pk>/', CashFlowUpdateView.as_view(), name='cash_flow-update'),
    path('cash_flow_delete/<int:pk>/', CashFlowDeleteView.as_view(), name='cash_flow-delete'),


    # Урлы для типов движения денежных средств
    path('type_create/', TypeCreateView.as_view(), name='type-create'),
    path('type_update/<int:pk>/', TypeUpdateView.as_view(), name='type-update'),
    path('type_delete/<int:pk>/', TypeDeleteView.as_view(), name='type-delete'),

    # Урлы для статусов движения денежных средств
    path('status_create/', StatusCreateView.as_view(), name='status-create'),
    path('status_update/<int:pk>/', StatusUpdateView.as_view(), name='status-update'),
    path('status_delete/<int:pk>/', StatusDeleteView.as_view(), name='status-delete'),

    # Урлы для категорий движения денежных средств
    path('category_create/', CategoryCreateView.as_view(), name='category-create'),
    path('category_update/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    path('category_delete/<int:pk>/', CategoryDeleteView.as_view(), name='category-delete'),

    # Урлы для подкатегорий движения денежных средств
    path('subcategory_create/', SubcategoryCreateView.as_view(), name='subcategory-create'),
    path('subcategory_update/<int:pk>/', SubcategoryUpdateView.as_view(), name='subcategory-update'),
    path('subcategory_delete/<int:pk>/', SubcategoryDeleteView.as_view(), name='subcategory-delete'),
]
