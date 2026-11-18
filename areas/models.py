from django.db import models


class Area(models.Model):
    headquarters = models.ForeignKey("sedes.Sede", on_delete=models.SET_NULL, null=True)
    manager = models.ForeignKey(
        "empleados.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_areas",
    )
    dept_name = models.CharField(unique=True)

    def __str__(self):
        return self.dept_name
