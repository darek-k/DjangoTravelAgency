from django import forms
from core.models import Continent


class ContinentForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = (
            'name',
        )

    name = forms.CharField(max_length=50)
