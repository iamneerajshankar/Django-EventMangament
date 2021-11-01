from django.shortcuts import render
from events import form
from events.form import VenueForm
from events.models import Event, MyClubUser, Venue
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def search_venue(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        venues = Venue.objects.filter(venue_place__contains= searched)
        return render(request, 'search_venues.html', {'searched' : searched, 'venues': venues})
    
    else:
        return render(request, 'search_venues.html')


# views for list of venues 
def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'venue-list.html', {'venue_list':venue_list})

def show_venue(request, venue_id):
    venue_detail = Venue.objects.get(pk=venue_id)

    return render(request, 'venue-detail.html',{'venue_detail':venue_detail})


def add_venue(request):
    submitted = False
    if request.method == "POST":
        modelForm = VenueForm(request.POST)
        if modelForm.is_valid():
            modelForm.save()
            return render(request, 'success.html')

    else:
        modelForm = VenueForm
        if 'submitted' in request.GET:
            submitted = True
 
    return render(request, 'venue-form.html', {'modelForm': modelForm, 'submitted':submitted})



def testHome(request):
    event_list = Event.objects.all()

    return render(request, 'demo.html', {'event_list': event_list})