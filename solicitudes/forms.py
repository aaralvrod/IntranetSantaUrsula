from django import forms
from .models import Request, Key, Vehicle, Place


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = "__all__"


class KeyForm(forms.ModelForm):
    class Meta:
        model = Key
        fields = "__all__"


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = "__all__"
