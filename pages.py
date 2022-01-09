import streamlit as st
import st_state_patch
import streamlit.components.v1 as components
from rtm import rtm_deck

def p1():
    st.write("""
        Hey There!
        I'm Kevin Mehta and Thanks for visiting my streamlit.
        
        I came across the job listing and am really interested because it complements my work experience and interests.

        Please checkout the sections above and I'd be happy to talk about them in further detail.

        On a professional note, I interned at Fidelity Investments, where I built full-stack real-time data science pipelines using ELK.
        At octopus, I wish to leverage these skills to help you build more resilient, affordable, & green power grids that are quick reactive to unexpected changes in capacity & proactivly accomodating for foreseable demands through ML forecasting.
        
        On a personal note, I am interested in networks & graph theory and what better network than the power grid?
        It's got the social aspect of serving people, economic aspect of markets, & all the enginnering!

        Kevin.Mehta@outlook.com
    """)    

def p2():
    st.write("These are the many technologies I have worked with in my journey, some extensively others lightly.")
    st.write("Feel free to ask me about my experience with any specific ones.")

    with st.expander(" 🛢️ Integrate data sources in pipelines"):
        st.write("I have incorporated various raw data sources in my pipelines. From stored procedures to deploying GET/POST apis in GCP to reading from splunk queries.")

        images = {
            "IBM DB2" : "https://www.db2tutorial.com/wp-content/uploads/2019/03/db2-tutorial.png",
            "Oracle DB": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuktzm6O1L75SydZTKiweeo7DVdUYZy-kakg&usqp=CAU",
            "Generic files": "https://stayfi.com/wp-content/uploads/2020/08/CSV-Icon.png",
            "Splunk": "https://www.splunk.com/content/dam/splunk2/images/2020-splunk-planet.svg",
            "Smart Meter Texas": "https://smartprepaidelectric-prd-webapp01.azurewebsites.net/portals/0/SMT%20Image.png",
            "Nasdaq": "https://media.glassdoor.com/sqll/12152/nasdaq-squarelogo-1522690440241.png",
            "ERCOT": "https://media.glassdoor.com/sqll/23282/ercot-squarelogo-1487707402908.png"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])
        
    with st.expander("👨🏻‍💻 Build, automate, deploy and maintain data pipelines"):
        #🔧
        st.write("I have built and deployed realtime pipelines spanning various services of Azure, and AWS.")
        st.write("I have limited familiarity with IBM pipeline builder & like services as well as AWS IAM practices.")

        images = {
            "Amazon Kinesis": "https://raw.githubusercontent.com/kimehta/octopus-streamlit/main/media/kinesis.png",
            "Apache Kafka": "https://cdn.confluent.io/wp-content/uploads/kafka-icon-blue.jpg"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])

    with st.expander("📊 Build dashboards"):
        #📱
        st.write("Dashboards I have built. From simple excel to pythonic streamlit. From public Google data studio to access controlled powerBI.")
        #"Tableau": "https://workforceedtech.org/wp-content/uploads/2019/03/Tableau_Logo_resized.png",
        images = {
            "streamlit": "https://streamlit.io/images/brand/streamlit-mark-color.svg",
            "powerBI": "https://apksshare.com/wp-content/uploads/2021/06/Microsoft-Power-BIBusiness-data-analytics-APK-MOD-Download-2.2.210514.2135005.png",
            "Anodot": "https://media.glassdoor.com/sql/2241975/anodot-squarelogo-1598434242364.png",
            "Kibana": "https://img.stackshare.io/service/1722/Image_2019-05-20_at_4.53.31_PM.png",
            "Google Data Studio": "https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])

    with st.expander("🧑🏾‍🤝‍🧑🏼 Collaborative development & deployment"):
        #🌐
        st.write("During my internship I developed & deployed a python ORM package on an internal JFrog artifcatory that was used by our teams across the world.")
        st.write("In addition, I have minimal experience with JIRA, TDD, & agile methodologies.")

        images = {
            "Gitlab": "https://about.gitlab.com/images/press/logo/png/gitlab-icon-rgb.png",
            "Jfrog": "https://img.stackshare.io/service/4711/jfrog-artifactory-logo.png",
            "Github": "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
            "TravisCI": "https://travis-ci.org/images/logos/TravisCI-Mascot-1.png",
            "Git": "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png",
            "CircleCI": "https://a.slack-edge.com/80588/img/plugins/circleci/service_512.png"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])
        
  
    with st.expander("⚙️ extraction, transformation, loading"):
        st.write("Unsurprising, coding is where I have the most experience coming from a CS major. I have worked with these and many more smaller blocks of the ETL.")
        st.write("I primarily use python, but have working experience with a trove of other languages, including custom ones like sparkSQL & googleJS")

        images = {
            "Python": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
            "DataJoint": "https://avatars.githubusercontent.com/u/2375501",
            "Google Apps Sctip": "https://www.gstatic.com/images/branding/product/2x/apps_script_48dp.png",
            "Apache Logstash": "https://img.stackshare.io/service/1683/preview.png",
            "Amazon Lambda": "https://raw.githubusercontent.com/kimehta/octopus-streamlit/main/media/lambda.png"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])

    with st.expander("📈 analytical, data-driven understanding "):
        #💱
        st.write("During my internship, I not only built & compared many industry leading anomaly detection solutions, but also built my own ML models to further explore pitfalls.")
        st.write("Feel free to ask me about my Machine learning & Statistical learning knowledge.")

        images = {
            "Amazon Forecast": "https://raw.githubusercontent.com/kimehta/octopus-streamlit/main/media/forecast.png",
            "Azure Anomaly Detector": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjD8cB33WDxO8INrUC3LGkTmmjdzGS0hME7dNwEgzz5izcheeA0tf8MCER6V5jWMgAyLE&usqp=CAU",
            "Anodot": "https://media.glassdoor.com/sql/2241975/anodot-squarelogo-1598434242364.png"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])
    
    with st.expander("☁️ large-scale batch and real-time data pipelines", expanded=True):
        st.write("Here's some of my pipelines spanning various cloud providers. Check Demos section for more info.")
        st.write("Some of these pipelines are live. I'd be happy to demo them and walk through the internals.")
        

        images = {
            "Electricity smart meter": "https://smartprepaidelectric-prd-webapp01.azurewebsites.net/portals/0/SMT%20Image.png",
            "ETL": "https://www.gstatic.com/images/branding/product/2x/apps_script_48dp.png",
            "storage": "https://kstatic.googleusercontent.com/files/adf55cdf4c7f8fb38efbf8df6c2792660fbeff2d05be05f2ec8e9c265a179b51c64b9679d8aee00e09cad19ce419d90a2d999b82cea4200abbe78c73e6bfaacf",
            "Dashboard": "https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])
        
        images = {
            "Infrastructure logs": "https://thumbs.dreamstime.com/b/tool-network-logo-icon-design-can-be-used-as-complement-to-127079485.jpg",
            "stream": "https://raw.githubusercontent.com/kimehta/octopus-streamlit/main/media/kinesis.png",
            "storage": "https://www.romexsoft.com/wp-content/uploads/2020/09/AWS-S3-min.png",
            "Analytics & Dashboard": "https://mpng.subpng.com/20180820/vgx/kisspng-amazon-com-amazon-web-services-amazon-redshift-ama-amazon-quicksight-logo-svg-vector-amp-png-transp-5b7b83c5ed0380.2616095715348213179708.jpg"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])

def p3():
    st.info("Please bear with the slow loadings, I am paying for hosting fees out of pocket and hence certain pipelines only boot up on demand for this demo.")
    st.info("If some pipeline is down, It's probably to reduce cost but I'd be happy to boot it live for a demo in an interview.")

    with st.expander("Real-Time Locational Prices from ERCOT"):
        col1, col2 = st.columns(2)
        with col1:
            st.write("Embedded iframe straight from ERCOT")
            components.iframe("https://www.ercot.com/content/cdr/contours/rtmLmpHg.html", height =800, width=750)
        
        with col2:
            st.write("Pull data from ERCOT API and visualize using pydeck")
            option = st.radio("Select Data", ["LMP","SPP"], index = int(bool(st.session_state.b3_e1_c2)), key="b3_e1_c2")

            deck, datestamp = rtm_deck(option)
            st.write(datestamp)
            st.pydeck_chart(deck)

    with st.expander("real-time order flow forecasting AWS pipeline"):
        st.write("feed live nasdaq trades data, forecast future trades per second from historical")
        images = {
            "Nasdaq": "https://media.glassdoor.com/sqll/12152/nasdaq-squarelogo-1522690440241.png",
            "python": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
            "stream": "https://raw.githubusercontent.com/kimehta/octopus-streamlit/main/media/kinesis.png",
            "storage": "https://www.romexsoft.com/wp-content/uploads/2020/09/AWS-S3-min.png",
            "Analytics & Dashboard": "https://mpng.subpng.com/20180820/vgx/kisspng-amazon-com-amazon-web-services-amazon-redshift-ama-amazon-quicksight-logo-svg-vector-amp-png-transp-5b7b83c5ed0380.2616095715348213179708.jpg"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])


    with st.expander("Hourly smart meter texas - google data studio GCP pipeline"):
        st.write("fully public, you may click on icons to observe.")
        images = {
            "Electricity smart meter": "https://smartprepaidelectric-prd-webapp01.azurewebsites.net/portals/0/SMT%20Image.png",
            "ETL": "https://www.gstatic.com/images/branding/product/2x/apps_script_48dp.png",
            "storage": "https://kstatic.googleusercontent.com/files/adf55cdf4c7f8fb38efbf8df6c2792660fbeff2d05be05f2ec8e9c265a179b51c64b9679d8aee00e09cad19ce419d90a2d999b82cea4200abbe78c73e6bfaacf",
            "Dashboard": "https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])

    with st.expander("realtime infrastructure performance - IBM WATSON ML pipeline"):

        st.write("Data comes from various infrastructure performance logs(cpu,ram,load,...).")
        st.write("In this demo, this streamlit is simulating an electrical generator data points(power level, temp, vibrations).")
        st.write("A neural network IN IBM ML that I built & trained produces a performance score.")
        st.write("scores farther from 0 indicate performance anomalies.")
        st.write("both raw data and performance scores can be sent to a dashboard.")
        st.write("")

        images = {
            "IBM Watson": "https://miro.medium.com/max/500/1*9Ue1zHmtrVvhMGCqZ6SQ6A.png"
        }
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[list(images.keys())[i]], width=100)
                st.write(list(images.keys())[i])

def p4():
    st.write("Some dubious observations regarding electricity")

    with st.expander("It is cheaper to produce electricity than to transmit it"):
        st.write("As you already know, cost of electricity generally is less than the TDU charge for transmission in Texas.")
        st.write("~70% of people in texas live within 50 miles roundtrip of a power plant")
        st.write("electric cars cost ~225Wh/mi to operate. that's ~11kWh or <$0.50 in electricity cost.")
        st.write("Most EVs have 65-75kWh battery pack, effectively giving 50-60kWh to spare after making the roundtrip.")
        st.write("cost of transffering 50kWh over grid = $2.3. cost of transffering in a car battery pack = $0.5 + operating cost.")
        st.write("Perhaps this makes sense for someone who lives offgrid & uses their vehicle battery to power their house.")
        st.write("More so in difficult to maintain grid areas like califorina. shifts billions in liabilities from grid operator to consumer.")
        st.write("I know this is stupid but I said dubious observations.")

    with st.expander("Alternative energy storage"):
        st.write("Lithium batteries are all the rage but refrigarent batteries have been around for a long time. why haven't they caught on?")
        st.write("The refrigerants are stored at high pressure, not at cold temperatures, and it is slowly evaporated during day time to cool the air in a closed loop.")
        st.write("Just like an AC but with bigger compressor and a refrigerant pool.")

    with st.expander("Integrate battery storage in grid"):
        st.text("""
        The Battery Energy Storage Task Force (BESTF) has made a number of policy recommendations to ERCOT.

        Considerations include 1) short-term battery storage for sporadic/emergency use 2) long-term under a "single model" as integral part of the grid.
        Octopus can help decentralize & democratize electricity production by encouraging their customers to use their BEV or other dense energy storage solutions such as thermal regrigerant based solutions. 
        This allows octopus to participate in the BES scheme without significant upfront battery hardware costs, while having safety net of the Nodal markets in case if customers choose not to participate.

        It seems like electricity transmission is about as expensive as generation. This sounds like data.
        It is much easier &cheaper to upload a video on Youtube than it is for Youtube to distribute it onwards.
        Why not do what they do and add local cache for electricity?

        Current battery storage integrated into grid as powerplants per EIA:
        """)
        components.iframe("https://atlas.eia.gov/datasets/eia::battery-storage/explore?filters=eyJTdGF0ZSI6WyJUZXhhcyJdfQ%3D%3D&location=30.895492%2C-98.618330%2C6.00",width=800,height=800)
