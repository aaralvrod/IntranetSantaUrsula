from django.db import models

class Permiso(models.Model):
    class Level(models.IntegerChoices):
        BASIC = 0
        MEDIUM = 1
        ADVANCED = 2
        ADMIN = 3
    id_area = models.ForeignKey("areas.Area", related_name='permisos', on_delete=models.PROTECT)
    level = models.IntegerField(choices=Level.choices, default=Level.BASIC)
