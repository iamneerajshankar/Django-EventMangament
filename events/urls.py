from django.urls import path
from events import views

urlpatterns = [
    path('', views.testHome, name="list-events"),
    path('add-venue', views.add_venue, name = "add-venue"),
    path('list_venues', views.list_venues, name='list-venues'),
    path('show_venue_details/<venue_id>', views.show_venue, name="show-venue"),
    
]
