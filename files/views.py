from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import csv

from events.models import Venue

# Generate Text File from Venue List 
def venue_text_file(request):
    response = HttpResponse(content_type= 'text/plain')
    response['Content-Disposition'] = 'attachement; filename= venues_list.txt'

    # designate the model
    venues = Venue.objects.all()

    #create blanck list
    lines = []

    #loop through the output data
    for venue in venues:
        lines.append(f'{venue.venue_place}\n{venue.address}\n{venue.zip_code}\n{venue.phone}\n{venue.web_address}\n{venue.email_address}\n\n\n')

    response.writelines(lines)
    return response

#Generate CSV file from the venue list
def venue_csv_file(request):
    downlaod_csv = HttpResponse(content_type= 'text/csv')
    downlaod_csv['Content-Disposition'] = 'attachement; filename = venue_list.csv'

    #Designate the Venue Model
    venues = Venue.objects.all()

    #Create a csv writter 
    writer = csv.writer(downlaod_csv)

    #add column heading to the csv file
    writer.writerow(['Venue Name', 'Address', 'Zip Code', 'Phone Number', 'Website','Email Address'])


    # Loop through the out from the model
    for venue in venues:
        writer.writerow([venue.venue_place, venue.address, venue.zip_code, venue.phone, venue.web_address, venue.email_address])


    return downlaod_csv