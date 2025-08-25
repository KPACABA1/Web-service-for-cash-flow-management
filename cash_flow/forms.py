from django.forms import BooleanField, ModelForm

from cash_flow.models import Type, Status, Category, Subcategory


class StyleFormMixin:
    """Класс для стилизации форм."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class TypeForm(StyleFormMixin, ModelForm):
    """Класс форма для типов движения денежных средств."""
    class Meta:
        model = Type
        fields = '__all__'


class StatusForm(StyleFormMixin, ModelForm):
    """Класс форма для статусов движения денежных средств."""
    class Meta:
        model = Status
        fields = '__all__'


class CategoryForm(StyleFormMixin, ModelForm):
    """Класс форма для категорий движения денежных средств."""
    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryForm(StyleFormMixin, ModelForm):
    """Класс форма для категорий движения денежных средств."""
    class Meta:
        model = Subcategory
        fields = '__all__'
