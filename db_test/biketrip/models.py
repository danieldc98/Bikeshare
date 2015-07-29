from django.db import models
import json
import urllib2

class Sex(models.Model):
	kind = models.CharField(max_length = 1)

class Person(models.Model):
    sex = models.ForeignKey(Sex)
    birthyear = models.IntegerField()



class Station(models.Model):
	name = models.CharField(max_length = 50)
	id_number = models.IntegerField()

class Trip(models.Model):
	trip_id = models.IntegerField()
	start_time = models.CharField(max_length = 16)
	stop_time = models.CharField(max_length = 16)
	bike_id = models.IntegerField()
	trip_duration_minutes = models.IntegerField()
	from_station = models.ForeignKey(Station, related_name='trip_from_station')
	to_station = models.ForeignKey(Station, related_name='trip_to_station')
	user = models.ForeignKey(Person)
	google_duration_minutes = models.IntegerField()
	def to_url_format(self):
		origin = str(self.from_station.name)
		destination = str(self.to_station.name)

		origin = origin.replace(' ', '+')
		origin = origin.replace('&', '%26')

		destination = destination.replace(' ', '+')
		destination = destination.replace('&', '%26')

		origin += ",Chicago"
		destination += ",Chicago"
		
		parameters = "origin="+origin+"&"+"destination="+destination+"&mode=bicycling"
		
		url = "https://maps.googleapis.com/maps/api/directions/json?"+parameters
		return url
	
	def make_http_request(self):
		url = self.to_url_format()
		serialized_data = urllib2.urlopen(url)
		data = json.load(serialized_data)
		return data

	def get_google_maps_duration_minutes(self):
		seconds = self.make_http_request()['routes'][0]['legs'][0]['duration']['value']
		return seconds/60
	def set_google_duration_minutes(self):
		self.google_duration_minutes = self.get_google_maps_duration_minutes()
