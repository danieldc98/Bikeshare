import csv
import tablib
import sys
import os

from django.core.wsgi import get_wsgi_application
sys.path.append('/home/apluser/Devel/db_test')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db_test.settings")
application = get_wsgi_application()
from django.conf import settings
from import_export import resources
from biketrip.models import *

line_reader = csv.reader(open('/home/apluser/Downloads/Divvy_Stations_Trips_2014_Q3Q4/Divvy_Trips_2014-Q4.csv'))
data = tablib.Dataset()
data.headers = line_reader.next()

tf = open('/home/apluser/Downloads/Divvy_Stations_Trips_2014_Q3Q4/trip_data.csv', 'r+')
pf = open('/home/apluser/Downloads/Divvy_Stations_Trips_2014_Q3Q4/person_data.csv', 'r+')

trip_data = tablib.Dataset()
person_data = tablib.Dataset()

while(True):#  :)
	try:
		#fills data with all columns
		row = line_reader.next()
		shouldAppend = True
		for col in range(0, len(row)):
			if row[col] == '':
				shouldAppend = False
				continue
			else:
				if (col == 0 or col == 3 or col == 4 or col == 5 or col == 7 or col ==11):
					row[col] = int(row[col])
				if (row[col] == 'Male'):
					row[col] = 'M'
				if (row[col] == 'Female'):
					row[col] = 'F'
		if shouldAppend:
			data.append(row)

	except:
		print "data filled successfully"
		break



#get column names from data into respective Databases
for i in range(0, 9):	
	trip_data.append_col(data.get_col(i), "test header, you should never see this")
	#print i
for j in range(10, 12):
	person_data.append_col(data.get_col(j), "test header, you should never see this")
	#print j
trip_data.headers = data.headers[0:(trip_data.width)]
person_data.headers = data.headers[10:12]



tf.write(trip_data.csv)
pf.write(person_data.csv)
print 'csv files written'


#create Sex, Person, Station, and Trip models
for i in range(0, len(data)):
	(s, s_created) = Sex.objects.get_or_create(kind = person_data[i][0])
	if s_created:
		s.save()
	(p, p_created) = Person.objects.get_or_create(sex = s, birthyear = person_data[i][1])
	p.save()

	(st_from, st_from_created) = Station.objects.get_or_create(name = trip_data[i][6], id_number = trip_data[i][5])
	if st_from_created:
		st_from.save()
	(st_to, st_to_created) = Station.objects.get_or_create(name = trip_data[i][8], id_number = trip_data[i][7])
	if st_to_created:
		st_to.save()


	(t, t_created) = Trip.objects.get_or_create(google_duration_minutes = 0,trip_id = trip_data[i][0], start_time = trip_data[i][1], stop_time = trip_data[i][2], bike_id = trip_data[i][3], trip_duration_minutes = trip_data[i][4], from_station = st_from, to_station = st_to, user = p)
	json_data = t.make_http_request()
	if json_data['status'] == "OK":
		t.google_duration_minutes = json_data['routes'][0]['legs'][0]['duration']['value']
	else:
		t.google_duration_minutes = 0
	t.save()
print 'models created'
