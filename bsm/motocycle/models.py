from django.db import models

# Create your models here.
from people.models import Rider
from people.models import PlayerSave


class Motocycle(models.Model):
    rider = models.OneToOneField(Rider, default=None)
    max_speed = models.IntegerField(default=0)
    acceleration = models.IntegerField(default=0)
    setting_front = models.IntegerField(default=0)
    setting_back = models.IntegerField(default=0)
    name = models.CharField(max_length=255, default='')
    save = models.ForeignKey(PlayerSave)



    def __str__(self):
        return self.name