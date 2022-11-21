from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone', max_length=25)
    web = models.URLField('Website Address')
    email_address = models.EmailField('Email Address')
    
    def __str__(self):
        return self.name

class SocialClubUser(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    
    def __str__(self):
        return self.f_name + ' ' + self.l_name

class Event(models.Model):
    name = models.CharField('Event Name', max_length=255)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, blank=True, null=True)
    # venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    # if no description then it can be left blank
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(SocialClubUser, blank=True)
    
    def __str__(self):
        return self.name
