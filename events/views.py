from django.shortcuts import redirect, render
from events import form
from events.form import EventForm, VenueForm
from events.models import Event, MyClubUser, Venue
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.




#************************Shows the list of venues****************************************
def list_venues(request):
    venue_list = Venue.objects.all().order_by('venue_place')
    return render(request, 'venue-list.html', {'venue_list':venue_list})

#************************Shows details about single venue********************************
def show_venue(request, venue_id):
    venue_detail = Venue.objects.get(pk=venue_id)

    return render(request, 'venue-detail.html',{'venue_detail':venue_detail})


#************************Add Venue*******************************************************
def add_venue(request):
    submitted = False
    if request.method == "POST":
        addVenueForm = VenueForm(request.POST)
        if addVenueForm.is_valid():
            addVenueForm.save()
            return HttpResponseRedirect('/add-venue?submitted=True')

    else:
        addVenueForm = VenueForm
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'add-venue.html', {'addVenueForm': addVenueForm, 'submitted':submitted})

def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(venue_place__contains= searched)
        return render(request, 'search_venues.html', {'searched' : searched, 'venues': venues})
    
    else:
        return render(request, 'search_venues.html')

#****************** Update the Venue Items ***********************************
def update_venue(request, venue_id):
    venueDetails = Venue.objects.get(pk=venue_id)
    updateVenueForm = VenueForm(request.POST or None, instance=venueDetails)
    if updateVenueForm.is_valid():
        updateVenueForm.save()
        return redirect('list-venues')
    return render(request, 'update-venue.html', {'updateVenueForm': updateVenueForm})

#*********************Delete a venue***********************************
def delete_venue(request, venue_id):
    delVenue = Venue.objects.get(pk=venue_id)
    delVenue.delete()
    return redirect('list-venues')


#******************Shows the list of events***********************************
def showEvents(request):
    event_list = Event.objects.all()

    return render(request, 'event-list.html', {'event_list': event_list})

#******************Adding a new Event******************************************
def add_event(request):
    submitted = False
    if request.method == "POST":
        addEventForm = EventForm(request.POST)
        if addEventForm.is_valid():
            addEventForm.save()
            return HttpResponseRedirect('/add-event?submitted=True')

    else:
        addEventForm = EventForm
        if 'submitted' in request.GET:
            submitted = True
    
    return render(request, 'add-event.html', {'addEventForm': addEventForm, 'submitted': submitted})

#*********************Update Events***********************************
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    updateEventForm = EventForm(request.POST or None, instance=event)
    if updateEventForm.is_valid():
        updateEventForm.save()
        return redirect('list-events')

    return render(request, 'update-event.html', {'updateEventForm': updateEventForm})