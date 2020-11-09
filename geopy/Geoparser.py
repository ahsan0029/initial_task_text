import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
from geotext import GeoText
import re
raw=[]
response = pd.read_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\dbpedia_location\dbpedia_location.csv") #Tweet_data\raw_tweet.csv
# for index, row in response.iterrows():
#     a=(str(row['Text']))
#     raw.append(a)
# print(raw) 
for index, row in response.iterrows():
    a=(str(row['Location']))
    raw.append(a) 
places=raw    
# letters_only = re.sub("[^a-zA-Z]"," ",str(raw))
#places=str(raw)
#print(letters_only)
#places = GeoText(letters_only)
print(places)
cities=places
# cities = list(places.countries)

#print(len(cities))
geolocator = Nominatim(user_agent='myuseragent')
lat_lon=[]

for city in cities: 
    #print(city)
    try:
        location = geolocator.geocode(city)
        if location:
            print(location.latitude, location.longitude)
            
            lat_lon.append(location)
    except GeocoderTimedOut as e:
        print("Error: geocode failed on input %s with message %s"(city, e))
             
#print(lat_lon)
df = pd.DataFrame(lat_lon, columns=['Country', 'Coordinates'])
df1= df[['Coordinates']]
df1.to_csv(r"C:\Users\insan\OneDrive\Desktop\task_initial\geopy\coordinate_location.csv",index = None)
#print(df.head(5))