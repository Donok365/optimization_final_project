import csv
import pandas as pd
import googlemaps
from datetime import datetime   
    
gmaps = googlemaps.Client(key= '')

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

matrix_existing_data 

np_matrix = open('distancematrix_file.csv')
csv_reader = csv.reader(np_matrix, delimiter=',')

for row in csv_reader:
    matrix_existing_data.append(row)
 
np_matrix.close()

starting_location = ('Boston', '42.36325261897069','-71.0857617716905')

for np in np_list:
    csv_write_row = []
    now = datetime.now()
    lat_long = starting_location[1] + ',' + starting_location[2]
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
    print(f"{starting_location[0]} -> {np}")
    matrix_new_data = csv_write_row

for rows in range(len(existing_matrix_data) + 1):
    if rows == 0:
        csv_write_data.append(matrix_new_data)
    else:
        matrix_existing_data[row - 1][0] == matrix_new_data[row - 1]
        csv_write_data.append(matrix_existing_data)
    
#print(csv_write_data)
with open('distancematrix_file', mode='w') as matrix_file:
    matrix_writer = csv.writer(matrix_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in csv_write_data:
        matrix_writer.writerow(row)


        
 