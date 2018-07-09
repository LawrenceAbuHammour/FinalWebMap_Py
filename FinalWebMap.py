#FinalWebMap.py
#By: Lawrence Abu-Hammour
#This program opens a web map using the folium library and displays markers for
#volcano data along with a popup that displays this information

import folium #WebMap Library
import pandas #Data Analysis Library
import os #Operating System Interface Library
import webbrowser #Web Browser Interface Library

data = pandas.read_csv('Volcanoes_USA.txt') #Read CSV data into dataframe using pandas
lat = list(data['LAT']) #Create a list for latitude of the volcano from this dataframe
lon = list(data['LON']) #Create a list for longitude of the volcano from this dataframe
elev = list(data['ELEV']) #Create a list for the elevation of the volcano from this dataframe
name= list(data["NAME"]) #Create a list for the names of these volcanoes from this dataframe

# Function Definition for Color Markers based on Elevation. Take elevation data as a input
# and returns a color to be used in the main script.
def color_production(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000<= elevation < 3000:
        return 'orange'
    else:
        return 'red'

def height_c(nm):                              #Function to have Variable Pop-Up Height based on the length of the string
    if len(str(nm)) <= 16:
        return "175"
    else:
        return "225"

#Create map object centered at a certain point
map = folium.Map(location = [38.58, -99.09], zoom_start = 4, tiles = 'Mapbox Bright')
#Create feature group for volcano layer
fgv = folium.FeatureGroup(name = 'Volcanoes')
#For Loop to iterate through dataframe lists and produce markers on the map corresponding to this data.
for lt, ln, el, nm in zip(lat, lon, elev, name):
    html = """
        <h1> %s </h1>
        <font color ="7531DE"> Elevation: %s m <br>
        Coordinates = %s , %s""" #Pop-Up Display Settings
        %(str(nm), str(el), str(round(float(lt), 2)), str(round(float(ln), 2)))

    iframe = folium.IFrame(html=html, width=200,height= height_c(nm))
    fgv.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup=folium.Popup(iframe),
    fill_color = color_production(el), color = 'grey', fill = True, fill_opacity = 0.7))

#Create feature group for population layer
fgp = folium.FeatureGroup(name = 'Population')
#Read Data from *.json file and format information onto the population layer of the map
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function = lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000 else 'orange'
if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#Add Volcano and Population layer
map.add_child(fgp)
map.add_child(fgv)
#Layer Control for toggling of different layers
map.add_child(folium.LayerControl())

#Save Map file as an html file.
map.save('FinalWebMap.html')

#Search for newly created file within the directory
filename = 'file:///'+os.getcwd()+'/' + 'FinalWebMap.html'
#Open a new tab in the default web browser using the newly created file as a destination
webbrowser.open_new_tab(filename)
