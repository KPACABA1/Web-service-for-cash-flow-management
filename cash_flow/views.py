from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from cash_flow.filters import CashFlowFilter
from cash_flow.forms import TypeForm, StatusForm, CategoryForm, SubcategoryForm
from cash_flow.models import CashFlow, Type, Status, Category, Subcategory


class CashFlowListView(FilterView):
    """Контроллер для просмотра всех моделей движения денежных средств."""
    model = CashFlow
    filterset_class = CashFlowFilter
    template_name = 'cash_flow_list.html'
    # Имя переменной в шаблоне
    context_object_name = 'cashflows'


class CashFlowCreateView(CreateView):
    """Контроллер для создания движения денежных средств."""
    model = CashFlow
    fields = ['status', 'type', 'category', 'subcategory', 'amount', 'comment']
    template_name = 'cash_flow_create.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')

    def get_context_data(self, **kwargs):
        """Метод для обновления подкатегорий при выборе категории."""
        context = super().get_context_data(**kwargs)
        # Добавляем URL для AJAX запроса в контекст шаблона
        context['get_subcategories_url'] = reverse_lazy('cash_flow:get_subcategories')
        return context


def load_subcategories(request):
    """Контроллер именно для обработки AJAX запросов в контроллере CashFlowCreateView."""
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return JsonResponse(list(subcategories.values('id', 'name')), safe=False)


class CashFlowUpdateView(UpdateView):
    """Контроллер для редактирования моделей движения денежных средств."""
    model = CashFlow
    fields = ['date_was_created', 'status', 'type', 'category', 'subcategory', 'amount', 'comment']
    template_name = 'cash_flow_update.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class CashFlowDeleteView(DeleteView):
    """Класс-контроллер для удаления моделей движения денежных средств."""
    model = CashFlow
    template_name = 'cash_flow_delete.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class TypeCreateView(CreateView):
    """Контроллер для создания типов движения денежных средств."""
    model = Type
    fields = ['name']
    template_name = 'type_create.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class TypeUpdateView(UpdateView):
    """Класс контролер для редактирования типов движения денежных средств."""
    model = Type
    form_class = TypeForm
    success_url = reverse_lazy('cash_flow:cash_flow-list')
    template_name = 'type_update.html'


class TypeDeleteView(DeleteView):
    """Класс-контроллер для удаления моделей типов движения денежных средств."""
    model = Type
    template_name = 'type_delete.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class StatusCreateView(CreateView):
    """Контроллер для создания статусов движения денежных средств."""
    model = Status
    fields = ['name']
    template_name = 'status_create.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class StatusUpdateView(UpdateView):
    """Класс контролер для редактирования статусов движения денежных средств."""
    model = Status
    form_class = StatusForm
    success_url = reverse_lazy('cash_flow:cash_flow-list')
    template_name = 'status_update.html'


class StatusDeleteView(DeleteView):
    """Класс-контроллер для удаления моделей статусов движения денежных средств."""
    model = Status
    template_name = 'status_delete.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class CategoryCreateView(CreateView):
    """Контроллер для создания категорий движения денежных средств."""
    model = Category
    fields = ['name']
    template_name = 'category_create.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class CategoryUpdateView(UpdateView):
    """Класс контролер для редактирования категорий движения денежных средств."""
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('cash_flow:cash_flow-list')
    template_name = 'category_update.html'


class CategoryDeleteView(DeleteView):
    """Класс-контроллер для удаления моделей категорий движения денежных средств."""
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class SubcategoryCreateView(CreateView):
    """Контроллер для создания подкатегорий движения денежных средств."""
    model = Subcategory
    fields = ('name', 'category')
    template_name = 'subcategory_create.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')


class SubcategoryUpdateView(UpdateView):
    """Класс контролер для редактирования подкатегорий движения денежных средств."""
    model = Subcategory
    form_class = SubcategoryForm
    success_url = reverse_lazy('cash_flow:cash_flow-list')
    template_name = 'subcategory_update.html'


class SubcategoryDeleteView(DeleteView):
    """Класс-контроллер для удаления моделей подкатегорий движения денежных средств."""
    model = Subcategory
    template_name = 'subcategory_delete.html'
    success_url = reverse_lazy('cash_flow:cash_flow-list')
