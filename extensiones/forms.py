from django import forms

from .models import ExtensionFija, ExtensionMovil, MobileDevice


class ExtensionMovilForm(forms.ModelForm):
    class Meta:
        model = ExtensionMovil
        fields = ["extension", "num_phone", "pin", "puk", "employee"]


class ExtensionFijaForm(forms.ModelForm):
    class Meta:
        model = ExtensionFija
        fields = ["extension", "num_phone", "employee", "area"]


class MobileDeviceForm(forms.ModelForm):
    class Meta:
        model = MobileDevice
        fields = [
            "type_device",
            "brand",
            "model",
            "serial_number",
            "imei",
            "imei2",
            "mobile_extension",
            "delivery_date",
            "return_date",
        ]
        widgets = {
            "delivery_date": forms.DateInput(attrs={"type": "date"}),
            "return_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        delivery = cleaned_data.get("delivery_date")
        return_d = cleaned_data.get("return_date")
        if delivery and return_d and return_d <= delivery:
            raise forms.ValidationError(
                "La fecha de devolución debe ser posterior a la fecha de entrega."
            )
        return cleaned_data
