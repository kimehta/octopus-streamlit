import streamlit as st

def header():
    
    col1, col2, col3, col4 = st.columns((1,3,3,3))
    #https://openclipart.org/image/400px/323162
    
    with col1:
        hh="""
        <style>
        div.e1tzin5v2:nth-child(1) > div > div > div > div.stButton > button {
            font-size: 20px;
            background: url(https://media.gettyimages.com/videos/neon-light-home-icon-animation-on-black-background-video-id1182862006?s=640x640) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
            color: rgb(255,255,255);
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b1 = st.button("Home")

    with col2:
        hh="""
        <style>
        div.e1tzin5v2:nth-child(2) > div > div > div > div.stButton > button {
            padding: 10px 10px;
            font-family: "Trebuchet MS", Arial, Verdana;  
            font-size: 20px;
            background: url(https://miro.medium.com/max/1200/0*ABgQRoSOxyHksOEo.gif) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
            color: rgb(255,255,255);
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b2 = st.button("Experience")

    with col3: 
        hh="""
        <style>
        div.e1tzin5v2:nth-child(3) > div > div > div > div.stButton > button {
            font-family: "Trebuchet MS", Arial, Verdana;  
            font-size: 20px;
            background: url(https://github.com/kimehta/octopus-streamlit/blob/main/3dgifmaker40906.gif?raw=true) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
            color: rgb(255,255,255);
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b3 = st.button("Demos")

    with col4: 
        hh="""
        <style>
        div.e1tzin5v2:nth-child(4) > div > div > div > div.stButton > button {
            font-size: 20px;
            background: url(https://miro.medium.com/max/1000/0*PpJM0VvDNpTERGdT.gif) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
            color: rgb(255,255,255);
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b4 = st.button("Ideas")
    return b1,b2,b3,b4