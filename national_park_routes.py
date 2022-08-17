import csv
import pandas as pd
import googlemaps
from datetime import datetime   
    
gmaps = googlemaps.Client(key='')

np_dict = {}
np_list = []

np_filein = open('Updated_input_Boston.csv')
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

for np in np_list:
    csv_write_row = []
    csv_write_row.append(np[0])
    for np_next in np_list:
        if np != np_next: #calculate distance from one park to every other (not itself)
            now = datetime.now()
            np_lat_long = str(np[1]) + ',' + np[2]
            np_next_lat_long = str(np_next[1]) + ',' + np_next[2]
            try:
                directions_result = gmaps.directions(np_lat_long,
                                                    np_next_lat_long,
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
        else: 
            dd_tuple = (0, 0) #Same National Park
            csv_write_row.append(f"{dd_tuple[0]};{dd_tuple[1]}")
        print(f"{np} -> {np_next}")
    csv_write_data.append(csv_write_row)
            
with open('distancematrix_file.csv', mode='w') as matrix_file:
    matrix_writer = csv.writer(matrix_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_write_data:
        matrix_writer.writerow(row)


        
 