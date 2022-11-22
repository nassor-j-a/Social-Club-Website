from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event

# Create your views here.

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
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})
