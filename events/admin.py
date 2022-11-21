from django.contrib import admin
from .models import Venue
from .models import SocialClubUser
from .models import Event

# Register your models here.
admin.site.register(Venue)
admin.site.register(SocialClubUser)
admin.site.register(Event)
