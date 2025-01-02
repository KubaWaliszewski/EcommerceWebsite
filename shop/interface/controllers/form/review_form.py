from django import forms
from ....infrastructure.orm.models import Review

from core.interface.constants import FIELD_STYLE


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)]),
            'comment': forms.Textarea(attrs={
                'rows': 5,
                **FIELD_STYLE
                }),
        }
