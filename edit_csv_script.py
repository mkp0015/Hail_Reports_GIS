#import dependencies (packages)
import numpy as np


#open data to create xy events
infile = r'C:\Users\mpullman\Desktop\ESS515_final\storm_events\storm_events_2006.csv'
with open(infile, 'r') as f:
    lines = f.readlines()

#redeclare lines variable to just include data and not header
lines = lines[1:]

#get dimensions of data
x_dim = len(lines[1].split(',')[:-1])
y_dim = len(lines)

#create blank array to hold data
longitude = np.zeros([y_dim,])
latitude = np.zeros([y_dim,])
month = np.zeros([y_dim,])
year = np.zeros([y_dim,])

#read data into blank array by column
for i in range(longitude.shape[0]):
    lon = lines[i].split(',')[8]
    lat = lines[i].split(',')[7]
    mm = lines[i].split(',')[0][4:6]
    yy = lines[i].split(',')[0][0:4]
    
    longitude[i,] = lon
    latitude[i,] = lat
    month[i,] = mm
    year[i,] = yy

#get spring data (march (3), april (4), may (5))
spring_months = [3., 4., 5.]
while month == spring_months:
    #longitude_spring = longiutde
    
#get summer data (june (6), july (7), august (8))

#get fall data (september (9), october (10), november (11))

#get winter data (december (12), january (1), february (2)) 

    
#save data into new txt file
np.savetxt(r'C:\Users\mpullman\Desktop\ESS515_final\storm_events\storm_events_2016_edit.csv', np.transpose([year, month, latitude, longitude]), delimiter=',', newline='\n', header = 'year, month, latitude, longitude') 
