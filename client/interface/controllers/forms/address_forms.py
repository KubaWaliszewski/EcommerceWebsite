from django import forms

from client.infrastructure.orm.models import Address
from core.interface.constants import FIELD_STYLE


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('first_name', 'last_name', 'address', 'address2', 'city', 'zip_code', 'country', 'phone',)
        widgets = {
            'first_name': forms.TextInput(attrs=FIELD_STYLE),
            'last_name': forms.TextInput(attrs=FIELD_STYLE),
            'address': forms.TextInput(attrs=FIELD_STYLE),
            'address2': forms.TextInput(attrs=FIELD_STYLE),
            'city': forms.TextInput(attrs=FIELD_STYLE),
            'zip_code': forms.TextInput(attrs=FIELD_STYLE),
            'country': forms.TextInput(attrs=FIELD_STYLE),
            'phone': forms.TextInput(attrs=FIELD_STYLE),
        }