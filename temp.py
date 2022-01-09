#import streamlit as st

#b0 = st.button("b0")
#b1 = st.button("b1")

#if 'g' not in st.session_state or b1: 
#    st.session_state.g = False

#if b0 or st.session_state.g:
#    with st.expander("expander"):
#        col1, col2 = st.columns(2)
#        with col1:

#            #if 'g' in st.session_state:
#            #    st.write(st.session_state.g)
#            option = st.radio("radio", ["one","two"], key="g")
            
##st.write(st.session_state.ce)



import pandas as pd
from html.parser import HTMLParser
import requests

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
    #longitude is 107

    x0 = -107.0
    y0 = 36.8
    x_scale = 0.023015
    y_scale = 0.01875
    
    points = pd.DataFrame()
    for area in parser.map:
        coords = area[1]
        x,y,z = [int(co) for co in area[1][1].split(',')]
        spp, price = area[2][1].split(':')

        price = price.split('$')[1]
        
        points = points.append({'lon':x0+(x_scale*x), 'lat':y0-(y_scale*y), 'name':spp, 'price':price},ignore_index=True)

    return points

def rtm_deck(source):

    d1 = get_df(source)
    
    tooltip = {
        "html":
            "<b>Name:</b> {name} <br/>"
            "<b>Price:</b> {price} $<br/>"
    }
    df = pd.DataFrame(data=d1)
    print(df)

rtm_deck("LMP")