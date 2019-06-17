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
        return 'blue'
    elif elev>2500:
        return 'red'
    else:
        return 'orange'

map = folium.Map(location=[45,-120], zoom_start=5)

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln in zip(lat,lon):
    # fg.add_child(folium.Marker(location=[lt, ln], popup=names[count]+" "+str(elevation[count])+" metres", icon=folium.Icon(color=color_producer(elevation[count]))))
    fgv.add_child(folium.CircleMarker(location=(lt, ln), popup=names[count]+" "+str(elevation[count])+" metres", radius=8, fill=True,
                                     fill_color = color_producer(elevation[count]), color='grey', fill_opacity = 1))
    count+=1

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function= lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                            else 'orange' if  10000000 < x['properties']['POP2005'] < 50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map2.html")



# print(type(data))
# print(LAT, LON)
# # print(data.loc[0:,"LAT":])