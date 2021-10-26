from django.db import models
from django.db.models import base, manager
from django.contrib.auth.models import User
from django.db.models.deletion import SET, SET_NULL

# Create your models here.
 
class Venue(models.Model):
    venue_place = models.CharField('Place of Event', max_length=200)
    venue_image = models.ImageField('Venue Picture',upload_to='pics')
    address = models.CharField('Venue Address', max_length=200)
    zip_code = models.CharField('Zip Code', max_length=100)
    phone = models.CharField('Contact Number', max_length=100)
    web_address =  models.URLField('Website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.venue_place


class MyClubUser(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=100)
    event_date = models.DateTimeField()
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField('Name of Venue', max_length=120)
    event_manager = models.ForeignKey(User, blank=True, null=True, on_delete=SET_NULL)
    description = models.TextField('Event Description')
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name


