import csv
import pandas as pd
import googlemaps
from datetime import datetime   
    
gmaps = googlemaps.Client(key='AIzaSyC47eSIAmH4WItXGqJ6Yxn9kuj0fVvl8HA')

np_dict = {}
np_list = []

np_filein = open('Updated_input_8_8_22.csv')
csv_reader = csv.reader(np_filein, delimiter=',')

header = []
header = next(csv_reader)

csv_write_data = []
csv_header_row = []

csv_header_row.append('Fill')
for row in csv_reader:
    np_in = [row[2], row[0], row[1]]
    np_list.append(np_in)
    csv_header_row.append(row[2])
    
np_filein.close()

csv_write_data.append(csv_header_row)

#geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

#now = datetime.now()

location = ('Boston', '42.36325261897069','-71.0857617716905')

for np in np_list:
    csv_write_row = []
    #csv_write_row.append(np[0])
    now = datetime.now()
    lat_long = location[1] + ',' + location[2]
    np_lat_long = np[1] + ',' + np[2]
    try:
        directions_result = gmaps.directions(np_lat_long,
                                             lat_long,
                                             mode="driving",
                                             departure_time=now,
                                             traffic_model='pessimistic',
                                             units='standard'
                                            )
            
        dd_tuple = (round(float(directions_result[0]['legs'][0]['distance']['value']) / 1609.34, 2), round(float(directions_result[0]['legs'][0]['duration']['value']) / 3600, 2))
        csv_write_row.append(f"{dd_tuple[0]};{dd_tuple[1]}") #convert distance to miles and duration to hours
    except:
        dd_tuple = ("N/A", "N/A")
        csv_write_row.append(f"{dd_tuple[0]};{dd_tuple[1]}")
    print(f"{location[0]} -> {np}")
    csv_write_data.append(csv_write_row)

#print(csv_write_data)
with open('distancematrix_file_8_8_22.csv', mode='w') as matrix_file:
    matrix_writer = csv.writer(matrix_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_write_data:
        matrix_writer.writerow(row)


        
 