from django.db import models

class Request(models.Model):
    id_key = models.ForeignKey("solicitudes.Key", related_name='requests', on_delete=models.PROTECT)
    id_vehicle = models.OneToOneField(
        "solicitudes.Vehicle",
        related_name='request',
        on_delete=models.PROTECT
    )
    id_place = models.ForeignKey("solicitudes.Place", related_name='requests', on_delete=models.PROTECT)
    id_employee = models.ForeignKey("empleados.Employee", related_name='requests', on_delete=models.PROTECT)
    
class Key(models.Model):
    name = models.CharField(unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    plate = models.CharField(unique=True)
    model = models.CharField()
    condition = models.TextField()
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.plate

class Place(models.Model):
    name = models.CharField(unique=True)
    type = models.CharField()
    detail = models.TextField()
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name