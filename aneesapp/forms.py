from django import forms
from .models import Event,Attendee,Ticket

class Eventform(forms.ModelForm):
    class Meta:
        model=Event
        fields= ['title','description','date','venue']
class AttendeeForm(forms.ModelForm):
    class Meta:
        model=Attendee
        fields=  ['name','email','phone_number']
class TicketForm(forms.ModelForm):
    class Meta:
        model=Ticket
        fields= ['attendee','seat_number','price','status']

