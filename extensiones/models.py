from django.db import models


class ExtensionMovil(models.Model):
    extension = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    num_phone = models.PositiveIntegerField(unique=True)
    pin = models.PositiveSmallIntegerField(unique=True)
    puk = models.PositiveSmallIntegerField(unique=True)
    employee = models.ForeignKey("empleados.Employee", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.num_phone)


class ExtensionFija(models.Model):
    extension = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    num_phone = models.PositiveIntegerField(unique=True)
    employee = models.ForeignKey("empleados.Employee", on_delete=models.PROTECT)
    area = models.ForeignKey("areas.Area", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.num_phone)


class MobileDevice(models.Model):
    type_device = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50)
    imei = models.CharField(max_length=50)
    imei2 = models.CharField(max_length=50)
    mobile_extension = models.ForeignKey("extensiones.ExtensionMovil", on_delete=models.PROTECT)
    delivery_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return f"{self.brand} {self.model} — {self.serial_number}"