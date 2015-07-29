from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    return HttpResponse("Hello, world!.")

def home(request):
    context = {'Trip_list' : Trip.objects.all()}
    return render(request, 'biketrip/index.html', context)
   
def data(request):
    male_riders = [person for person in Person.objects.all() if person.sex.kind == 'M']
    male_percent = round(100 * float(len(male_riders)) / len(Person.objects.all()), 2)
    female_percent = 100 - male_percent
    avg_birthyear = avg(Person.objects.all())
    avg_age = 2015 - avg_birthyear
    num_commuters = 0
    num_tourists = 0
    num_fast = 0
    total_minutes = 0
    total_trips = 0
    for trip in Trip.objects.all():
        if trip.google_duration_minutes != 0:
       	    total_minutes += trip.trip_duration_minutes
            total_trips += 1
            if (trip.trip_duration_minutes - trip.google_duration_minutes) > 30:
                num_tourists += 1
            elif abs(trip.trip_duration_minutes - trip.google_duration_minutes) <= 15:
                num_commuters += 1
            if trip.google_duration_minutes - trip.trip_duration_minutes > 10:
		num_fast += 1 
    tourist_percent = round(100 * num_tourists / float(total_trips), 2)
    avg_duration = total_minutes / total_trips
    fast_percent = round(100 * num_fast / float(total_trips), 2)

    oldest_age = 0
    for person in Person.objects.all():
        if (2015-person.birthyear) > oldest_age:
            oldest_age = 2015 - person.birthyear

    context = {'male_percent' : male_percent, 'female_percent' : female_percent, 'avg_age' : avg_age, 'tourist_percent' : tourist_percent, 'avg_duration' : avg_duration, 'oldest_age' : oldest_age, 'fast_percent' : fast_percent}
    return render(request, 'biketrip/left-sidebar.html', context)

def avg(l):
    total = 0
    for p in l:
        total += p.birthyear
    return round(float(total)/len(l), 2) 

# Create your views here.
