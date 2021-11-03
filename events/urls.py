from django.urls import path
from files.views import venue_text_file, venue_csv_file
from events import views


urlpatterns = [
    path('', views.showEvents, name="list-events"),
    path('add-venue', views.add_venue, name = "add-venue"),
    path('list_venues', views.list_venues, name='list-venues'),
    path('show_venue_details/<venue_id>', views.show_venue, name="show-venue"),
    path('searched-venues', views.search_venue, name="search-venue"),
    path('update-venues/<venue_id>', views.update_venue, name="update-venue"),
    path('delete-venue/<venue_id>', views.delete_venue, name='delete-venue'),
    path('add-event', views.add_event, name = "add-event"),
    path('update-event/<event_id>', views.update_event, name='update-event'),
  

    #**********File Handling Urls***********************
  path('download-text-files', venue_text_file, name='text-file'),
  path('download-spreadsheet-file', venue_csv_file, name='spreadsheet-file'),

]
