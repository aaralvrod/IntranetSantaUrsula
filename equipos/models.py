from django.db import models
from django.core.validators import EmailValidator

class Proveedor(models.Model):
    num_phone = models.PositiveIntegerField(unique=True)
    name = models.CharField()
    email = models.EmailField(validators=[EmailValidator()], unique=True)
    company = models.CharField()
    cif = models.CharField()

    def __str__(self):
        return self.name

class Equipo(models.Model):
    class Status(models.TextChoices):
        ACTIVO = 'ACTIVO', 'Activo'
        INACTIVO = 'INACTIVO', 'Inactivo'
        MANTENIMIENTO = 'MANTENIMIENTO', 'Mantenimiento'

    ip = models.PositiveIntegerField(unique=True)
    brand = models.CharField()
    availability = models.BooleanField(default=True)
    model = models.CharField()
    hostname = models.CharField()
    user = models.CharField()
    serial_num = models.PositiveIntegerField(unique=True)
    screens_num = models.PositiveIntegerField()
    delivery_date = models.DateField(auto_now=False)
    status = models.CharField(max_length=15, choices=Status.choices)
    operating_system = models.CharField()
    antivirus = models.CharField()
    ens = models.CharField()
    encryption = models.CharField()
    location = models.CharField()
    floor = models.PositiveIntegerField()
    purchase_date = models.DateField(auto_now=False)
    warranty_date = models.DateField(auto_now=False)
    observation = models.TextField()
    provider = models.ForeignKey("equipos.Proveedor", related_name='equipos', on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.serial_num)

class Prestamo(models.Model):
    equipment = models.ForeignKey("equipos.Equipo", on_delete=models.PROTECT)
    employee = models.ForeignKey("empleados.Employee", on_delete=models.PROTECT)
    asignation_datetime = models.DateTimeField(auto_now_add=True)
    expiration_datetime = models.DateTimeField(auto_now=False)
    observations = models.TextField()
    
    def __str__(self):
        return f"Préstamo {self.equipment} ({self.employee})"

class Screen(models.Model):
    brand = models.CharField()  
    model = models.CharField()
    serial_num = models.PositiveIntegerField(unique=True)
    status = models.CharField(max_length=15, choices=Equipo.Status.choices)
    equipment = models.ForeignKey("equipos.Equipo", on_delete=models.PROTECT)
    
    def __str__(self):
        return str(self.serial_num)

class Peripherals(models.Model):
    status = models.CharField(max_length=15, choices=Equipo.Status.choices)
    type_peripheral = models.CharField()
    brand = models.CharField()
    model = models.CharField()
    warranty = models.DateField(auto_now=False)
    provider = models.ForeignKey("equipos.Proveedor", on_delete=models.PROTECT)
    
    def __str__(self):
        return self.type_peripheral

class Printer(models.Model):
    ip = models.PositiveIntegerField(unique=True)
    model = models.CharField()
    brand = models.CharField()
    type_printer = models.CharField()
    area = models.ForeignKey("sedes.Sede", on_delete=models.PROTECT)
    provider = models.ForeignKey("equipos.Proveedor", on_delete=models.PROTECT)    
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.ip})"