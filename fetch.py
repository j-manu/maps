import datetime
import time
import googlemaps
import csv

KEY=''
gmaps = googlemaps.Client(key=KEY)

tomorrow_date = datetime.date.today() + datetime.timedelta(days=1)
start_time = datetime.time(7,0)
start_date_time = datetime.datetime.combine(tomorrow_date, start_time)

days = 7
timegap = datetime.timedelta(minutes=30)
total_measurements = 25
travel_modes = ['driving', 'transit']
transit_modes = ['bus', 'rail']

with open('results.csv', 'w') as f:
  w = csv.writer(f)
  w.writerow(['departure_time', 'start_address', 'end_address', 'mode', 'transit_mode',
              'distance_in_metres', 'time_in_seconds'])


def fetch_and_save_result(origin, destination, departure_time, travel_mode, transit_mode=None):
  directions_result = gmaps.directions(origin,
                                      destination,
                                      mode=travel_mode,
                                      transit_mode=transit_mode,
                                      departure_time=departure_time)
  row = {}
  leg = directions_result[0]['legs'][0]
  with open('results.csv', 'a') as f:
    w = csv.writer(f)
    w.writerow([departure_time, leg['start_address'], leg['end_address'],
                 travel_mode, transit_mode, leg['distance']['value'], leg['duration']['value']])

with open('places.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=':')
    for row in csv_reader:
      for day in range(days):
        for i in range(total_measurements):
          date_time = start_date_time + datetime.timedelta(days=day) + timegap * i
          for travel_mode in travel_modes:
            if travel_mode == 'transit':
              for transit_mode in transit_modes:
                fetch_and_save_result(row[0], row[1], date_time, travel_mode, transit_mode)
            else:
              fetch_and_save_result(row[0], row[1], date_time, travel_mode)
