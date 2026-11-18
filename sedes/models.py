from django.db import models

class Sede(models.Model):
    name = models.CharField(unique=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Floor(models.Model):
    floor_num = models.PositiveSmallIntegerField(unique=True, primary_key=True)
    floor_name = models.CharField(unique=True)
    
    def __str__(self):
        return self.floor_name


class Telecommunications(models.Model):
    type_telecommunications = models.CharField(max_length=100)
    serial_num = models.PositiveIntegerField(unique=True)
    num = models.PositiveIntegerField(unique=True)
    assignment = models.CharField(max_length=100)
    num_admin = models.CharField(max_length=100)
    speed = models.CharField(max_length=100)
    headquarters = models.ForeignKey("sedes.Sede", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.serial_num)