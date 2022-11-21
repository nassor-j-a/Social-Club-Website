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
]