from django.contrib import admin
from .models import League, Division, Team, Player

# Register your models here.

admin.site.register(League)
admin.site.register(Division)
admin.site.register(Team)
admin.site.register(Player)