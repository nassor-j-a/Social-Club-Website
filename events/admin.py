from django.contrib import admin
from .models import Venue
from .models import SocialClubUser
from .models import Event

# Register your models here.
# admin.site.register(Venue)
admin.site.register(SocialClubUser)
# admin.site.register(Event)

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    # changes the display of items on the main page
    list_display = ('name', 'address', 'phone')
    
    # makes the ordering(of the name field) be in an alpabetically order
    # ('-name') inverts the ordering(from Z to A)
    ordering = ('name',)
    search_fields = ('name', 'address')

# admin.site.register(Venue, VenueAdmin)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    # applying a filter
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
