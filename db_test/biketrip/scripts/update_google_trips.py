import biketrip.models
from biketrip.models import *

for trip in Trip.objects.all():
	if trip.google_duration_minutes == 0:
		json_data = trip.make_http_request()
		if json_data['status'] == "OK":
			trip.google_duration_minutes = json_data['routes'][0]['legs'][0]['duration']['value']
		else:
			print "Max queries hit"
			break
