from django import forms
from .models import Permiso

class PermisoForm(forms.ModelForm):
    class Meta:
        model = Permiso
        fields = ['id_area', 'level']
