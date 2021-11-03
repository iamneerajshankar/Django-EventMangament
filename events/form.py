from django import forms 
from django.forms import ModelForm, fields, widgets
from events.models import Venue, Event

# Create the form here 
class VenueForm(ModelForm):
    class Meta:

        model = Venue
        fields = ('venue_place', 'address', 'zip_code', 'phone', 'web_address', 'email_address')

        labels = {
            'venue_place': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web_address': '',
            'email_address': ''
        }

        widgets = {
            'venue_place': forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Venue Name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Address'}),
            'zip_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' :'Area Code'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder' :'Phone'}),
            'web_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder' :'Website'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder' :'Email Address'})
        }
#******************Creating Event from the model***********************************
class EventForm(ModelForm):
    class Meta: 

        model = Event
        fields =  ('name', 'event_date', 'venue', 'event_manager', 'description', 'attendees')

        labels = {
            'name': '',
            'event_date': '',
            'venue': '',
            'event_manager': '',
            'description' : '',
            'attendess': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'event_date': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Event Date',}),
            'venue': forms.Select(attrs={'class': 'form-control','placeholder': 'Place of Event',}),
            'event_manager': forms.Select(attrs={'class': 'form-control','placeholder': 'Manager',}),
            'description' : forms.Textarea(attrs={'class': 'form-control','placeholder': 'Description',}),
            'attendess': forms.SelectMultiple(attrs={'class': 'form-control','placeholder': 'Attendees',})
        }


    