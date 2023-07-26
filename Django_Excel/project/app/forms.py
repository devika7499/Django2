
from django import forms
from .models import WellData
class PresonForm(forms.Form):
    class meta:
        model=WellData
        fields='__all__'