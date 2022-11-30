from django.shortcuts import render, redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.http import HttpResponseRedirect
from .models import Event, Venue
from .forms import VenueForm, EventForm

# Create your views here.

#  Delete Venue
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venue')

# Delete Event
def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')


def home(request, year=datetime.now().year, 
         month=datetime.now().strftime('%B')):
    name = "Doha"
    
    # the context dictionary after home.html allows us to pass context from the backend to the frontend
    
    # return render(request, 'home.html', {"fname": name})
    
    # return render(request, 'home.html', {"fname": name, "year": year, "month": month})
    
    # Capitalizes the first letter in the month name/ Matches the name to the default lib name in the url
    month = month.title()
    # Convert month from name to calendar
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    
    # creating a calendar
    cal = HTMLCalendar().formatmonth(year, month_number)
    
    # get current year
    now = datetime.now()
    current_year = now.year
    
    # get current time
    current_time = now.strftime('%I:%M:%S %p')
    
    return render(request, 'events/home.html', {"fname": name, 
                             "year": year, "month": month, 
                             "month_number": month_number, "cal": cal, 
                             "current_year": current_year, 
                             "current_time": current_time})


def all_events(request):
    
    # fetching all items from the database model
    # .order_by('name') sorts the list by name in alphabetical order
    event_list = Event.objects.all().order_by('name')
    
    # .order_by('-name')/.order_by('name').reverse() sorts the list by name in reverse alphabetical order
    # event_list = Event.objects.all().order_by('-name')
    # event_list = Event.objects.all().order_by('name').reverse()
    
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})
    

def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html',
                    {'form': form, 'submitted': submitted})


def list_venue(request):
    # .order_by('name') sorts the list by name in alphabetical order
    venue_list = Venue.objects.all().order_by('name')
    
    # .order_by('?')sorts the list by name in random order
    # venue_list = Venue.objects.all().order_by('?')
    
    # .order_by('-name')/.order_by('name').reverse() sorts the list by name in reverse alphabetical order
    # venue_list = Venue.objects.all().order_by('-name')
    # venue_list = Venue.objects.all().order_by('name').reverse()

    
    return render(request, 'events/venue.html',
                    {'venue_list': venue_list})
    
def show_venue(request, venue_id):
    
    # fetching individual items from the database model
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html',
                    {'venue': venue})
    
def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html',
                    {'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html',
                    {})
        
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venue')
    return render(request, 'events/update_venue.html', 
                  {'venue': venue, 'form': form})
    
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html',
                    {'form': form, 'submitted': submitted})
    
def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    return render(request, 'events/update_event.html', 
                  {'event': event, 'form': form})