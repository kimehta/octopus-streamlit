import streamlit as st

def a_p():
    with st.expander(" 🛢️ plan new data sources and pipelines"):
        st.text("Data sources I have worked with")

        images = ["https://www.db2tutorial.com/wp-content/uploads/2019/03/db2-tutorial.png",
                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuktzm6O1L75SydZTKiweeo7DVdUYZy-kakg&usqp=CAU",
                  "https://stayfi.com/wp-content/uploads/2020/08/CSV-Icon.png",
                  "https://www.splunk.com/content/dam/splunk2/images/2020-splunk-planet.svg",
                  "https://smartprepaidelectric-prd-webapp01.azurewebsites.net/portals/0/SMT%20Image.png",
                  "https://media.glassdoor.com/sqll/12152/nasdaq-squarelogo-1522690440241.png",
                  "https://media.glassdoor.com/sqll/23282/ercot-squarelogo-1487707402908.png"
                  ]
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[i], width=100)
        
    with st.expander("👨🏻‍💻 Build, automate, deploy and maintain data pipelines"):
        #🔧
        st.text("launguages & technologies amazon iam")

    with st.expander("📊 Build dashboards"):
        #📱
        st.text("Dashboards I have built")

        images = ["https://streamlit.io/images/brand/streamlit-mark-color.svg",
                  "https://workforceedtech.org/wp-content/uploads/2019/03/Tableau_Logo_resized.png",
                  "https://apksshare.com/wp-content/uploads/2021/06/Microsoft-Power-BIBusiness-data-analytics-APK-MOD-Download-2.2.210514.2135005.png",
                  "https://media.glassdoor.com/sql/2241975/anodot-squarelogo-1598434242364.png",
                  "https://img.stackshare.io/service/1722/Image_2019-05-20_at_4.53.31_PM.png",
                  "https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg"
                  ]
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[i], width=100)

    with st.expander("🧑🏾‍🤝‍🧑🏼 Collaborative development & deployment"):
        #🌐
        st.text("ci/cd git opensource navi artifactory")
        st.text("UK, US, Germany, Spain, Japan and NZ")
        st.text("Work with the global data platform team to deploy new tools and services into the US data environment ; Participate in and contribute to our global data community")

        images = ["https://about.gitlab.com/images/press/logo/png/gitlab-icon-rgb.png",
            "https://img.stackshare.io/service/4711/jfrog-artifactory-logo.png",
            "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
            "https://travis-ci.org/images/logos/TravisCI-Mascot-1.png",
            "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png",
            "https://a.slack-edge.com/80588/img/plugins/circleci/service_512.png"
            ]
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[i], width=100)
        
  
    with st.expander("⚙️ extraction, transformation, loading"):
        st.text("data from a wide variety of data sources")
        images = ["https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
            "https://avatars.githubusercontent.com/u/2375501",
            "https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png",
            "https://travis-ci.org/images/logos/TravisCI-Mascot-1.png",
            "https://git-scm.com/images/logos/downloads/Git-Icon-1788C.png",
            "https://a.slack-edge.com/80588/img/plugins/circleci/service_512.png"
            ]
        columns = st.columns(len(images))
        for i in range(len(columns)):
            with columns[i]:
                st.image(images[i], width=100)

    with st.expander("📈 analytical, data-driven understanding "):
        #💱
        st.text("fast changing business")  
    
    with st.expander("☁️ large-scale batch and real-time data pipelines", expanded=True):
        st.text("Amazon Web Services, Azure or GCP cloud platform")
        st.text("Here's some of my pipelines")
        st.image("https://www.romexsoft.com/wp-content/uploads/2020/09/AWS-S3-min.png",width=100)

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.image("https://smartprepaidelectric-prd-webapp01.azurewebsites.net/portals/0/SMT%20Image.png",width=100)
            st.text("data source")
        with col2:
            st.image("https://www.gstatic.com/images/branding/product/2x/apps_script_48dp.png",width=100)
            st.text("compute")
        with col3:
            st.image("https://kstatic.googleusercontent.com/files/adf55cdf4c7f8fb38efbf8df6c2792660fbeff2d05be05f2ec8e9c265a179b51c64b9679d8aee00e09cad19ce419d90a2d999b82cea4200abbe78c73e6bfaacf",width=100)
            st.text("storage")
        with col4:
            st.image("https://www.gstatic.com/analytics-suite/header/suite/v2/ic_data_studio.svg",width=100)
            st.text("dashboard")

def b_p():pass
def c_p():pass