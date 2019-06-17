import folium
import pandas

# print(help(folium.Map))

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[45,-120], zoom_start=5)
fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat,lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Marker", icon=folium.Icon(color='red')))

map.add_child(fg)
map.save("Map2.html")



# print(type(data))
# print(LAT, LON)
# # print(data.loc[0:,"LAT":])