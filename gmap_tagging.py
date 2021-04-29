
import pandas as pd
import gmplot
data = pd.read_csv('spatial_network.csv')
data.head()

# latitude and longitude list 
latitude_list = data['LATITUDE'] 
longitude_list = data['LONGITUDE'] 

# center co-ordinates of the map 
gmap = gmplot.GoogleMapPlotter( 56.730876,9.349849,9)

# plot the co-ordinates on the google map 
gmap.scatter( latitude_list, longitude_list, 'red', size = 40, marker = True) 

# the following code will create the html file view that in your web browser 
gmap.heatmap(latitude_list, longitude_list) 

gmap.draw( "mymap.html" )
