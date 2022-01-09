import navbar
from pages import *
import streamlit as st
#import st_state_patch

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

b1,b2,b3,b4 = navbar.header()

if 'b3_e1_c2' not in st.session_state or b1 or b2 or b4: 
    st.session_state.b3_e1_c2 = False

if b1: p1()
if b2: p2()
elif b3 or st.session_state.b3_e1_c2: p3()
elif b4: p4()