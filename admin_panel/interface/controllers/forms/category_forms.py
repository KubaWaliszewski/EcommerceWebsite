from django import forms

from shop.infrastructure.orm.models import Category
from core.interface.constants import FIELD_STYLE


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={
                **FIELD_STYLE,
                'placeholder': 'Enter category name'
            })
        }