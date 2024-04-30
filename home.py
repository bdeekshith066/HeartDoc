import streamlit as st

def app():
    

    # Introduction
    gradient_text_html = """
        <style>
        .gradient-text {
            font-weight: bold;
            background: -webkit-linear-gradient(left, #07539e, #4fc3f7, #ffffff);
            background: linear-gradient(to right, #07539e, #4fc3f7, #ffffff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            display: inline;
            font-size: 3em;
        }
        </style>
        <div class="gradient-text">HeartDoc</div>
        """

    st.markdown(gradient_text_html, unsafe_allow_html=True) 
    st.write("AI-driven heart care, prediction, and personalized insights with HeartDoc.") 
    st.image('divider.png')
   
    

# Display custom HTML code
    
    st.write('Cardiovascular diseases (CVDs) are the :orange[leading cause of death globally], taking an estimated :orange[17.9 million lives each year].  \n CVDs are a group of disorders of the heart and blood vessels and include coronary heart disease, cerebrovascular disease, rheumatic heart disease and other conditions.  \n  More than :orange[four out of five CVD deaths] are due to heart attacks and strokes, and one third of these deaths occur prematurely in people under 70 years of age.')
    st.write('')
    st.write('')
    col4, col5,col7, col6 = st.columns([0.03,0.45,0.07,0.5])
    with col5:
        st.video("https://youtu.be/fv7yuJby4Rg?si=oKubCOh4hpQVxMtE")
    

    with col6:
        tab0,tab1, tab2 = st.tabs(["Facts", "Symptoms", "Prevention"])

        with tab0:
            st.subheader('Facts')
            st.write("- :orange[27% of deaths in India] are caused by cardiovascular diseases")
            st.write("- On an average of :orange[56,000 people die each day] or one death :orange[every 1.5 seconds] by cardiovascular diseases .")
            st.write("- According to the Cleveland Clinic, :orange[90% of heart disease] is treatable and preventable by: eating foods that are low in salt and cholesterol, exercising regularly, and not smoking.")
            st.write('')
            st.write("- Check out the personalized page for more customized information based on your requirements")

        with tab1:
            st.subheader("Symptoms of Cardiovascular Diseases:")
            st.write("- :orange[Chest Pain or Discomfort]: Persistent chest pain or discomfort, often described as tightness, pressure, or squeezing. ")
            st.write("- :orange[Shortness of Breath]: Difficulty breathing or sudden shortness of breath, especially during physical activity or at rest")
            st.write("- :orange[Heart Palpitations]: Irregular heartbeat, rapid heart rate, or sensations of skipped heartbeats.")
            st.write("- :orange[Fatigue]: Unexplained fatigue, weakness, or feeling unusually tired, even with minimal exertion.")
            st.write("- :orange[Swelling]: Swelling in the legs, ankles, or feet due to fluid retention (edema).")
            st.write('')
            st.write('Although these are common symptoms, they may not always indicate heart disease. For more information, visit our personalized page and prediction tool for tailored insights')


        with tab2:
            st.subheader("Preventions of Cardiovascular Diseases:")
            st.write("- :orange[Maintain a Healthy Die]: Eat a balanced diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats. ")
            st.write("- :orange[Regular Physical Activity]:  Engage in regular exercise, such as brisk walking, cycling, or swimming, for at least 150 minutes per week.")
            st.write("- :orange[Manage Blood Pressure]:  Monitor and control blood pressure levels through lifestyle modifications (e.g., reduced salt intake) and medication if prescribed")
            st.write("- :orange[Quit Smoking]:  Avoid tobacco and nicotine products, and seek support to quit smoking to reduce the risk of heart disease.")
            st.write("- :orange[Manage Stress]: Practice stress-reducing techniques such as meditation, yoga, or deep breathing exercises.")
            st.write('')
            st.write('Follow the above steps  to promote overall heart health and well-being.  \n :orange[Nothing beats a healthy heart] ')


    st.image('divider.png')
    st.write('')
    st.write('')
    st.write('')
    
    
if __name__ == "__main__":
    app()