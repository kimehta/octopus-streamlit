import requests
import pandas as pd
import streamlit as st
import pydeck as pdk
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = False
        self.datestamp = None
        self.map = []
    def handle_starttag(self, tag, attrs):
        if tag == "area": self.map.append(attrs)
        elif tag == "div" and attrs:
            if attrs[0][1] == "datestamp":
                self.recording = True
    def handle_endtag(self, tag):
        self.recording = False
    def handle_data(self, data):
        if self.recording:
            self.datestamp = data

def get_df(source):

    if source == 'LMP':
        r = requests.get('https://www.ercot.com/content/cdr/contours/rtmLmpHg.html').text
    else:
        r = requests.get('https://www.ercot.com/content/cdr/contours/rtmSpp.html').text

    parser = MyHTMLParser()
    parser.feed(r)

    lon0 = -107.0
    lat0 = 36.8
    lon_scale = 0.023015
    lat_scale = 0.01875
    
    points = pd.DataFrame()
    for area in parser.map:
        coords = area[1]
        x,y,z = [int(co) for co in area[1][1].split(',')]
        spp, price = area[2][1].split(':')

        price = price.split('$')[1]
        
        points = points.append({'lon':lon0+(lon_scale*x), 'lat':lat0-(lat_scale*y), 'name':spp, 'price':price},ignore_index=True)

    return points, parser.datestamp

def rtm_deck(source):

    d1, datestamp = get_df(source)
    
    tooltip = {
        "html":
            "<b>Name:</b> {name} <br/>"
            "<b>Price:</b> {price} $<br/>"
    }
    df = pd.DataFrame(data=d1)

    #view = pdk.data_utils.compute_view(df[["lon", "lat"]])
    #view.pitch = 75
    #view.zoom = 6
    #view.bearing = 60

    view = pdk.ViewState(
         latitude=30.9982,
         longitude=-98.6949,
         zoom=5,
         pitch=50,
     )

    column_layer = pdk.Layer(
        "ColumnLayer",
        data=df,
        get_position=["lon", "lat"],
        get_elevation="price*10",
        elevation_scale=100,
        radius=5000,
        get_fill_color=[250,250,250, 140],
        pickable=True,
        auto_highlight=True,
    )

    h3layer = pdk.Layer(
        "ScatterplotLayer",
        df,
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=6,
        radius_min_pixels=1,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=["lon", "lat"],
        get_radius="5000",
        get_fill_color=["price*2", 100, "price*4",100],
        get_line_color=[0, 0, 0,0],
    )


    r = pdk.Deck(
        layers=[column_layer, h3layer],
        initial_view_state=view,
        tooltip=tooltip
    )

    return r, datestamp