from django import forms
from .models import Proveedor, Equipo, Prestamo, Screen, Peripherals, Printer


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = "__all__"


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = "__all__"
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "purchase_date": forms.DateInput(attrs={"type": "date"}),
            "warranty_date": forms.DateInput(attrs={"type": "date"}),
        }


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = "__all__"
        widgets = {
            "expiration_datetime": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = "__all__"


class PeripheralsForm(forms.ModelForm):
    class Meta:
        model = Peripherals
        fields = "__all__"
        widgets = {
            "warranty": forms.DateInput(attrs={"type": "date"}),
        }


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = "__all__"
