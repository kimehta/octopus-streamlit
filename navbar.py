import streamlit as st

def header():
    
    col1, col2, col3 = st.columns(3)

    with col1:
        hh="""
        <style>
        div.e1tzin5v2:nth-child(1) > div > div.e1tzin5v1 > div.stButton > button {
            padding: 10px 10px;
            font-family: "Trebuchet MS", Arial, Verdana;  
            font-size: 20px;
            background: url(https://miro.medium.com/max/1200/0*ABgQRoSOxyHksOEo.gif) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b1 = st.button("Experience")

    with col2: 
        hh="""
        <style>
        div.e1tzin5v2:nth-child(2) > div > div.e1tzin5v1 > div.stButton > button {
            font-family: "Trebuchet MS", Arial, Verdana;  
            font-size: 20px;
            background: url(https://github.com/kimehta/octopus-streamlit/blob/main/3dgifmaker40906.gif?raw=true) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b2 = st.button("Skills")

    with col3: 
        hh="""
        <style>
        div.e1tzin5v2:nth-child(3) > div > div.e1tzin5v1 > div.stButton > button {
            font-size: 20px;
            background: url(https://miro.medium.com/max/1000/0*PpJM0VvDNpTERGdT.gif) no-repeat;
            border-radius: 16px;
            background-size: cover;
            height: 5em;
            width: 100%;
        }
        </style>"""
        st.markdown(hh, unsafe_allow_html=True)
        b3 = st.button("Ideas")
    return b1,b2,b3