from django import forms
from .models import Sede, Floor, Telecommunications

class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ["name", "address"]

class FloorForm(forms.ModelForm):
    class Meta:
        model = Floor
        fields = ["floor_num", "floor_name"]

class TelecommunicationsForm(forms.ModelForm):
    class Meta:
        model = Telecommunications
        fields = "__all__"
