from django import forms

from .models import Employee, VacationDays


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "dni",
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "is_manager",
            "headquarters",
            "area",
            "permissions",
        ]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            "dni",
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "is_manager",
            "headquarters",
            "area",
            "permissions",
            "mail_box",
            "mobile_extension",
            "landline_extension",
            "vacation_days",
        ]
        widgets = {
            "birth_date": forms.DateInput(attrs={"type": "date"}),
        }


class VacationDaysForm(forms.ModelForm):
    class Meta:
        model = VacationDays
        fields = ["employee", "start_date", "end_date"]
        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and end <= start:
            raise forms.ValidationError(
                "La fecha de fin debe ser posterior a la fecha de inicio."
            )
        return cleaned_data
