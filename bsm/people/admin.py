from django.contrib import admin

# Register your models here.
from people.models import Coach
from people.models import Rider
from people.models import Person
from people.models import PlayerSave
from people.models import Player

admin.site.register(Player)
admin.site.register(PlayerSave)
admin.site.register(Person)
admin.site.register(Rider)
admin.site.register(Coach)

