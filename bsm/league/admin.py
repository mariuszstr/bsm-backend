from django.contrib import admin

# Register your models here.
from league.models import Country
from league.models import City
from league.models import LeagueClass
from league.models import League
from league.models import Team

admin.site.register(Country)
admin.site.register(City)
admin.site.register(League)
admin.site.register(LeagueClass)
admin.site.register(Team)


