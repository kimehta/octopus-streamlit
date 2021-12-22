from collections import namedtuple
import navbar
from pages import *
import altair as alt
import math
import pandas as pd
import streamlit as st

st.set_page_config(
     page_title="kevin mehta",
     page_icon="https://tech.octopus.energy/assets/img/constantine.png",
     layout="wide",
     initial_sidebar_state="auto",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
)

#"""Work with the data scientists and data analysts to scope out and plan new data sources and pipelines
#Build, automate, deploy and maintain data pipelines
#Build Streamlet data apps and lend a hand building and maintaining Tableau dashboards
#Work with the global data platform team to deploy new tools and services into the US data environment
#Participate in and contribute to our global data community
#Build the infrastructure required for optimal extraction, transformation, and loading of data from a wide variety of data sources
#Use an analytical, data-driven approach to drive a deep understanding of fast changing business
#Build large-scale batch and real-time data pipelines with data processing frameworks in Amazon Web Services, Azure or GCP cloud platform
#"""

#st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")

b1,b2,b3 = navbar.header()

if b1: a_p()
if b2: b_p()
if b3: c_p()


#import geopandas as gpd
#shapefile = gpd.read_file("C:\Users\chicken\Downloads\PowerPlants_US_EIA\PowerPlants_US_202004.shp")
#print(shapefile)
#with st.echo(code_location='below'):
#    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
#    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

#    Point = namedtuple('Point', 'x y')
#    data = []

#    points_per_turn = total_points / num_turns

#    for curr_point_num in range(total_points):
#        curr_turn, i = divmod(curr_point_num, points_per_turn)
#        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
#        radius = curr_point_num / total_points
#        x = radius * math.cos(angle)
#        y = radius * math.sin(angle)
#        data.append(Point(x, y))

#    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
#        .mark_circle(color='#0068c9', opacity=0.5)
#        .encode(x='x:Q', y='y:Q'))