from django.contrib import admin
from .models import Event,Attendee,Ticket

# Register your models here.
admin.site.register(Event)
admin.site.register(Attendee)
admin.site.register(Ticket)

