from django.contrib import admin
from django.db.models import fields
from events.models import Event, MyClubUser, Venue


# Register your models here.
#admin.site.register(Event)
admin.site.register(MyClubUser)
#admin.site.register(Venue)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    # to display field when adding any venue
    fields = ('venue_place','venue_image', 'address', 'zip_code', 'phone', 'web_address', 'email_address')
    # To add columns to venues home page
    list_display = ('venue_place', 'address')
    #add search field to venue list 
    search_fields = ('venue_place', 'address')
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'event_manager', 'description', 'attendees' )
    list_display = ('name', 'event_date', 'event_manager')
    search_fields = ('name', 'event_manager')
    list_filter = ('name', 'event_date', 'event_manager')
    ordering = ('-event_date',)
    
