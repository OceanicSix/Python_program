import gmplot
# gmplot contains a simple wrapper around
# Google’s geocoding service enabling map initilization to the location of your choice.
gmap = gmplot.GoogleMapPlotter(-37.812015244225677, 144.951471202974, 15) # latitude and longitude of melbourne city

from pymongo import MongoClient

client = MongoClient()

db = client.fit5148_db
week12 = db.week12
# Preparing the data for plotting
unoccupiedList = []

# Looping through all the data
for row in week12.find():
    # Checking if the parking spot is available
    if row['status'] == 'Unoccupied':
        # Adding the latitude and longitude to the list of unoccupied spots
        unoccupiedList.append((float(row['latitude']), float(row['longitude'])))

    # The step below is required by the gmap scatter function to prepare data in correct format
unoccupied_lats, unoccupied_lons = zip(*unoccupiedList)
    # Plotting the points on the map

gmap.scatter(unoccupied_lats, unoccupied_lons, '#FF4500', size=10, marker=True)
print(len(unoccupied_lons))
print(len(unoccupied_lats))
for i in range(len(unoccupied_lats)):
    gmap.marker(unoccupied_lats[i],unoccupied_lons[i], title="A street corner in Seattle")

import webbrowser
# Drawing the map
gmap.draw("availableParkings.html")
webbrowser.open_new("availableParkings.html")