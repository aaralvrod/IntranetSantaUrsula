from django.db import models
from django.core.validators import EmailValidator

class Employee(models.Model):
    dni = models.CharField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    birth_date = models.DateField()
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    is_manager = models.BooleanField(default=False)
    mail_box = models.ForeignKey("shared.MailBox", on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    mobile_extension = models.ForeignKey("extensiones.ExtensionMovil", on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    landline_extension = models.ForeignKey("extensiones.ExtensionFija", on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    vacation_days = models.ForeignKey("empleados.VacationDays", on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    headquarters = models.ForeignKey("sedes.Sede", on_delete=models.PROTECT)
    area = models.ForeignKey("areas.Area", on_delete=models.PROTECT)
    permissions = models.ForeignKey("permisos.Permiso", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class VacationDays(models.Model):
    employee = models.ForeignKey("empleados.Employee", on_delete=models.PROTECT)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.start_date} to {self.end_date}"