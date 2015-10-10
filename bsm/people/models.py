from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Player(models.Model):
    """ More fields for User model """
    user = models.OneToOneField(User, related_name="ApiUser")
    hours = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class PlayerSave(models.Model):
    player = models.OneToOneField(Player, default=None, null=True, blank=True) # if empty, initial save for all players
    name = models.CharField(max_length=255, default='') # if empty, initial save for player
    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=255, default='')
    second_name = models.CharField(max_length=255, default='')
    save_name = models.ForeignKey(PlayerSave, null=True, blank=True)
    determination = models.IntegerField(default=0)
    ambition = models.IntegerField(default=0)
    professionalism = models.IntegerField(default=0)
    loyalty = models.IntegerField(default=0)
    reflex = models.IntegerField(default=0)
    date_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.second_name

class Rider(models.Model):
    person = models.OneToOneField(Person)
    start = models.IntegerField(default=0)
    corner = models.IntegerField(default=0)
    pair_raid = models.IntegerField(default=0)
    save_name = models.ForeignKey(PlayerSave, null=True, blank=True)

    def __str__(self):
        return self.person.to_string()





class Coach(models.Model):
    person = models.OneToOneField(Person)
    training = models.IntegerField(default=0)
    youth_training = models.IntegerField(default=0)
    manager_skill = models.IntegerField(default=0)
    physical_training = models.IntegerField(default=0)
    psychic_training = models.IntegerField(default=0)
    save_name = models.ForeignKey(PlayerSave, null=True, blank=True)

    def __str__(self):
        return self.person.to_string()
