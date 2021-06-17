from django.contrib import admin
from .models import Participant,Profile,Program,Location,Feedback

admin.site.register(Participant)
admin.site.register(Profile)
admin.site.register(Program)
admin.site.register(Location)
admin.site.register(Feedback)

# Register your models here.
