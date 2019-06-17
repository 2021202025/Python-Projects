import folium
import pandas

# print(help(folium.Map))

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
names = list(data["NAME"])
elevation = list(data["ELEV"])
count = 0

def color_producer(elev):
    if elev<1500:
        return 'green'
    elif elev>2500:
        return 'red'
    else:
        return 'orange'

map = folium.Map(location=[45,-120], zoom_start=5)
fg = folium.FeatureGroup(name="My Map")


for lt, ln in zip(lat,lon):
    # fg.add_child(folium.Marker(location=[lt, ln], popup=names[count]+" "+str(elevation[count])+" metres", icon=folium.Icon(color=color_producer(elevation[count]))))
    fg.add_child(folium.CircleMarker(location=(lt, ln), popup=names[count]+" "+str(elevation[count])+" metres", radius=5, fill=True,
                                     fill_color = color_producer(elevation[count]), color='grey', fill_opacity = 1))
    count+=1

map.add_child(fg)
map.save("Map2.html")



# print(type(data))
# print(LAT, LON)
# # print(data.loc[0:,"LAT":])