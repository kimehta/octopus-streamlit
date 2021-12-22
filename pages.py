import streamlit as st

def a_p():
    with st.expander("📡 🛢️ ☁️ plan new data sources and pipelines"):
        st.text("Here's some of my pipelines")
        st.image("https://www.romexsoft.com/wp-content/uploads/2020/09/AWS-S3-min.png",width=100)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image("https://www.smartmetertexas.com/images/logo-white.png",width=100)
            st.text("data API")
        with col2:
            st.image("https://www.gstatic.com/images/branding/product/2x/apps_script_48dp.png",width=100)
            st.text("ETL")
        with col3:
            st.image("https://kstatic.googleusercontent.com/files/adf55cdf4c7f8fb38efbf8df6c2792660fbeff2d05be05f2ec8e9c265a179b51c64b9679d8aee00e09cad19ce419d90a2d999b82cea4200abbe78c73e6bfaacf",width=100)
            st.text("storage")
        with col4:
            st.image("https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg",width=100)
            st.text("dashboard")

    with st.expander("👨🏻‍💻 🔧 Build, automate, deploy and maintain data pipelines"):
        st.text("launguages & technologies")

    with st.expander("📊 📱 Build dashboards"):
        st.text("streamlit, tableue, powerbi, datastudio, kibana")

    with st.expander("🧑🏾‍🤝‍🧑🏼 Collaborative development & deployment"):
        st.text("ci/cd git opensource navi artifactory")
        st.text("UK, US, Germany, Spain, Japan and NZ")
        st.text("Work with the global data platform team to deploy new tools and services into the US data environment ; Participate in and contribute to our global data community")
  
    with st.expander("🧑🏾‍🤝‍🧑🏼 extraction, transformation, loading"):
        st.text("data from a wide variety of data sources")  

    with st.expander("🧑🏾‍🤝‍🧑🏼 analytical, data-driven understanding "):
        st.text("fast changing business")  
    
    with st.expander("🧑🏾‍🤝‍🧑🏼 large-scale batch and real-time data pipelines"):
        st.text("Amazon Web Services, Azure or GCP cloud platform")

def b_p():pass
def c_p():pass