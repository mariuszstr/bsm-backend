from django.db import models
from people.models import PlayerSave


class Country(models.Model):
   name = models.CharField(max_length=255, default='')
   save = models.ForeignKey(PlayerSave)
   speedway_popularity = models.IntegerField(default=0)
   population = models.IntegerField(default=0)
   wealth = models.IntegerField(default=0)
   def __str__(self):
        return self.name


class City(models.Model):
   name = models.CharField(max_length=255, default='')
   save = models.ForeignKey(PlayerSave)
   speedway_popularity = models.IntegerField(default=0)
   population = models.IntegerField(default=0)
   wealth = models.IntegerField(default=0)
   def __str__(self):
        return self.name

class League(models.Model):
   name = models.CharField(max_length=255, default='')
   save = models.ForeignKey(PlayerSave)
   country = models.ForeignKey(Country)
   ability = models.IntegerField(default=0)
   def __str__(self):
        return self.name

class LeagueClass(models.Model):
    name = models.CharField(max_length=255, default='')
    league = models.ForeignKey(League)
    next_class = models.ForeignKey("self", default=None, null=True, blank=True, related_name="class_next_class")
    last_class = models.ForeignKey("self", default=None, null=True, blank=True, related_name="class_last_class")
    save = models.ForeignKey(PlayerSave)


    ability = models.IntegerField(default=0)
    number_of_promotions = models.IntegerField(default=0)
    number_of_drop = models.IntegerField(default=0)
    number_of_promotions_match = models.IntegerField(default=0)
    number_of_drop_match = models.IntegerField(default=0)
    league_script = models.TextField(default='')  # script for season
    match_script = models.TextField(default='')  # script for match
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255, default='')
    save = models.ForeignKey(PlayerSave)

    league = models.ForeignKey(League)
    league_class = models.ForeignKey(LeagueClass)
    matches = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    def __str__(self):
        return self.name

