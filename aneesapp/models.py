from django.db import models
from datetime import date
from django.utils import timezone

A=[
   ('a','Booked'),
   ('b','Cancelled'),
   ('c','Checked_in'),
]
# Create your models here.
class Event(models.Model):
   title=models.CharField(max_length=100)
   description= models.TextField()
   date = models.DateTimeField(default=timezone.now) 
   venue=models.CharField(max_length=200)
   created_at=models.DateTimeField(auto_now_add=True)
   def __str__(self):
      return self.title

class Attendee(models.Model):
    name =models.CharField(max_length=100)
    email=models.EmailField()
    phone_number=models.CharField(max_length=100)
    registered_at =models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name
    
class Ticket(models.Model):
   event=models.ForeignKey(Event,on_delete=models.CASCADE)
   attendee =models.ForeignKey(Attendee,on_delete=models.CASCADE)
   seat_number=models.CharField(max_length=100)
   price=models.IntegerField()
   status=models.CharField(max_length=5,choices=A)
   created_at =models.DateTimeField(auto_now_add=True)
   def __str__(self):
       return str(self.event) 