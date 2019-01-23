import folium
import pandas as pd

#Load data of volcanoes in USA
data = pd.read_csv('C:/Users/SYED/Desktop/Python/11. Flask Work/data/Volcanoes_USA.txt')
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#Create base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "Mapbox bright")

for lat, lon, elevation in zip(lat, lon, elevation):
    folium.Marker(location=[lat, lon], popup=str(elevation)+" m", icon=folium.Icon(color = 'gray')).add_to(map)

map.save("map1.html")
