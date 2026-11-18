from django.db import models
from django.core.validators import EmailValidator


class MailBox(models.Model):
    manager = models.ForeignKey("empleados.Employee", on_delete=models.PROTECT, related_name="managed_mailboxes")
    headquarters = models.ForeignKey("sedes.Sede", on_delete=models.PROTECT)
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    