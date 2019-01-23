import folium

map = folium.Map(location=[37.296933,-121.9574983], zoom_start=8, tiles = "Mapbox bright")

folium.Marker(location=[37.296933,-121.9574983], popup='Google HQ', icon=folium.Icon(color='blue')).add_to(map)

map.save("map1.html")
