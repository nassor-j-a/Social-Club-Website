from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    
    # Path Converters ~ they give route to urls
    # int: numbers, str: strings, 
    # paths: whole urls & /, 
    # slugs: hyphen - and underscores _,
    # UUID: Universally unique identifier
    path('<int:year>/<str:month>', views.home, name="home"),
    path('events', views.all_events, name="list-events"),
    path('add_venue', views.add_venue, name="add-venue"),
    path('list_venue', views.list_venue, name="list-venue"),
    path('show_venue/<venue_id>', views.show_venue, name="show-venue"),
    path('search_venues', views.search_venues, name="search-venues"),
    path('update_venue/<venue_id>', views.update_venue, name="update-venue"),
    path('add_event', views.add_event, name="add-event"),
    path('update_event/<event_id>', views.update_event, name="update-event"),
    path('delete_event/<event_id>', views.delete_event, name="delete-event"),
    path('delete_venue/<venue_id>', views.delete_venue, name="delete-venue"),
]