# FinalWebMap_Py
# By: Lawrence Abu-Hammour
#Introduction
Using the Python programming language, I programmed a web map that reads latitude and longitude data of marked volcanoes in the United States from a *.csv file and reads country and map border polygon data from a *.json file. The map also uses transparent colors to mark and represent population density from 2005 within a certain region. This program was an exercise in utilizing basic object-oriented Python programming, the folium, pandas, os, and webbrowser standard libraries in Python, and file interaction. Must install all the files provided for this program to function properly. Published in July 2018.

#How To Use

To utilize the Python program, you must have the folium, os, webbrowser, and pandas standard libraries installed on your python interpretor of your choice.

Once you have installed all the necessary files and the python program itself, run the program as you normally would any python program through the commmand line terminal. For this purpose, I prefer to use Atom and any command line packages that exists because it's more efficient to view the code and run it through that terminal.

Once you run the program within your command line terminal, the FinalPointMap.html file will appear within the folder that the files were installed in and will automatically open in your default browser. You can use your mouse to point and click on any of the volcano markers to view the height of the volcano and its precise location on the map through latitude and longitude data as a popup. In addition, the name of the volcano will be displayed in bold.

You may use the button in the upper right hand corner to toggle each layer of the map: Population and Volcano. One of the known issues encountered was that, at present, the program will start with the volcano marker layer on top of the transparent population layer. However, once you toggle the volcano layer followed by the populaton layer, the volcano markers will be hidden behind the population layer. At this current moment, the team at Folium is implementing a fix which will be available in the Folium v.0.6 where a method known as keep_in_front(*args) will keep a certain layer in front regardless of the order in which they are toggled.

#For Future Release

- Update App to include changes in folium v.6.0 which will utilize the keep_in_front method to keep a layer in front of other layers.
- Include User-Input Feature to allow users to update the map as they see fit with the location of volcanoes or other significant spot.
- Allow users to save and load a new version of the map that may include user-input data
- Allow continuous polygon layers rather than keeping it within one area of the map. This is to say that if you scroll further to the left or right as most maps would, the polygons are no longer defined.
