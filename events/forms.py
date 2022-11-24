from django import forms 
from django.forms import ModelForm
from .models import Venue

# Create a venue form
class VenueForm(ModelForm):
    # Defines the things in the class(Applies for Django. Not python generally???)
    class Meta:
      model = Venue
    #   considers all fields in the model
    #   fields = "__all__"
      
    #   individually defines the fields you want to add
      fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
      labels = {
          'name' : '',
          'address' : '',
          'zip_code' : '',
          'phone' : '',
          'web' : '',
          'email_address' : '',
      }
      
      widgets = {
          'name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue Name'}),
          'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
          'zip_code' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zip Code'}),
          'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}),
          'web' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Web Address'}),
          'email_address' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
      }