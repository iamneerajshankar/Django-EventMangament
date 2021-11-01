from django import forms 
from django.forms import ModelForm, fields
from events.models import Venue

# Create the form here 
class VenueForm(ModelForm):
    class Meta:

        model = Venue
        fields = ('venue_place', 'address', 'zip_code', 'phone', 'web_address', 'email_address')