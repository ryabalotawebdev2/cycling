from django.contrib import admin
from .models import Participant,Membership,Event,Location,Status

admin.site.register(Participant)
admin.site.register(Membership)
admin.site.register(Event)
admin.site.register(Location)
admin.site.register(Status)

# Register your models here.
