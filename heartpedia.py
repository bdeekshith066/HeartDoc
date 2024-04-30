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
        <div class="gradient-text">HeartPedia</div>
        """

    st.markdown(gradient_text_html, unsafe_allow_html=True) 
    st.write("Your go-to resource for understanding heart health, featuring a comprehensive library of heart disease terms and insights tailored for everyone.") 
    st.image('divider.png')

    st.write('')

    col1, col2, col3, col4 = st.columns([1,1,1,1])
    with col1:
        st.button('Heart Attack')
        st.write('')
        st.write('')
        st.write('')
        st.button('Hypertension(High BP)')
        st.write('')
        st.write('')
        st.write('')
        st.button('Atherosclerosis')
        st.write('')
        st.write('')
        st.write('')
        st.button('Stent')

    with col2:
        st.button('Cardiac Arrest')
        st.write('')
        st.write('')
        st.write('')
        st.button('Heart Failure')
        st.write('')
        st.write('')
        st.write('')
        st.button('Cholesterol')
        st.write('')
        st.write('')
        st.write('')
        st.button('Pacemaker')

    with col3:
        st.button('Coronary Artery Disease')
        st.write('')
        st.write('')
        st.write('')
        st.button('Electrocardiogram (ECG)')
        st.write('')
        st.write('')
        st.write('')
        st.button('Stroke')
        st.write('')
        st.write('')
        st.write('')
        st.button('Holter Monito')
    
    
    with col4:
        st.button('CPR')
        st.write('')
        st.write('')
        st.write('')
        st.button('Angina Pectoris')
        st.write('')
        st.write('')
        st.write('')
        st.button('Peripheral Artery Disease')
        st.write('')
        st.write('')
        st.write('')
        st.button('Systolic/Diastolic Blood Pressure')

    st.image('divider.png')


    def get_pedia_info(user_input):
        pedia_info = {
            "cpr": """ :orange[CPR (Cardiopulmonary Resuscitation)]  \n CPR is a life-saving emergency procedure involving chest compressions and rescue breaths to manually circulate blood and oxygen when someone's heart or breathing has stopped.  \n :orange[Importance]  \n - Early initiation of CPR can double or triple survival rates during cardiac arrest.  \n - CPR helps maintain vital blood flow to the brain and other organs until advanced medical care is available.  \n - Training in CPR is essential for individuals to respond effectively to emergencies and save lives.  \n
            Enter the name of a term from the HeartPedia to know more about it  """,


            "heart attack" : """ :orange[Heart Attack (Myocardial Infarction)]  \n  A heart attack occurs when blood flow to a part of the heart muscle is blocked, leading to damage or death of the affected heart tissue.  \n :orange[Symptoms]  \n - Chest pain or discomfort, often described as pressure, squeezing, or burning.  \n -  Shortness of breath, sweating, nausea, and pain radiating to the arm, jaw, or back.  \n - Women and older adults may experience atypical symptoms such as fatigue, nausea, or dizziness.  \n  :orange[importance]  \n - Prompt recognition of heart attack symptoms and calling emergency services (911) is crucial for timely treatment.  \n - Treatment options include medications (aspirin, nitroglycerin), angioplasty, or coronary artery bypass surgery.  \n - Rehabilitation and lifestyle changes (diet, exercise, smoking cessation) are vital for recovery and prevention of future events.  \n
            Enter the name of a term from the HeartPedia to know more about it.""",

            "cardiac arrest": """ :orange[Cardiac Arrest]  \n Cardiac arrest is a sudden loss of heart function, breathing, and consciousness, usually due to an electrical malfunction in the heart.  \n :orange[Importance]  \n -Cardiac arrest is different from a heart attack and requires immediate intervention with CPR and use of an automated external defibrillator (AED).  \n - Survival rates decrease by 7-10% for every minute without CPR or defibrillation.  \n -  Effective bystander CPR can significantly increase the chances of survival and reduce disability.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",



            "coronary artery disease": """:orange[Coronary Artery Disease (CAD)]  \n CAD is a condition where the coronary arteries become narrowed or blocked due to the buildup of plaque, reducing blood flow to the heart.  \n :orange[Risk Factors]  \n - High cholesterol, high blood pressure, smoking, diabetes, obesity, sedentary lifestyle, family history.  \n - Age, gender (men have a higher risk at younger ages; risk increases for women after menopause).  \n - Stress, poor diet (high in saturated fats and sugars), excessive alcohol consumption.  \n :orange[Importance]  \n -CAD is the leading cause of heart attacks and requires comprehensive management of risk factors.  \n - Treatment involves lifestyle modifications (diet, exercise), medications (statins, blood thinners), and interventions (angioplasty, stenting, bypass surgery).  \n - Preventive measures include regular check-ups, cholesterol screenings, and early detection and treatment of risk factors.  \n     
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "hypertension(high bp)" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "hypertension" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "high bp" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "hypertension" : """:orange[Hypertension (High Blood Pressure)]  \n Hypertension is persistently elevated blood pressure, which increases the workload on the heart and blood vessels.  \n :orange[Risks]  \n - Increases the risk of heart disease, stroke, kidney disease, and vision problems.  \n - Hypertension is often asymptomatic and can remain undetected for years, leading to silent organ damage.  \n - Risk factors include family history, age, obesity, high salt intake, and lack of physical activity.  \n :orange[Importance]  \n - Regular blood pressure monitoring is essential for early detection and management of hypertension.  \n -Lifestyle changes (dietary modifications, exercise) and medications (antihypertensives) are key to controlling blood pressure.  \n - Untreated hypertension can lead to serious complications, emphasizing the importance of adherence to treatment plans.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "heart failure" : """:orange[Heart Failure (Congestive Heart Failure)]  \n Heart failure occurs when the heart is unable to pump blood efficiently to meet the body's needs.  \n :orange[Symptoms]  \n - Shortness of breath, especially during physical activity or when lying flat.  \n - Fatigue, weakness, and swelling in the legs, ankles, or abdomen.  \n -Sudden weight gain due to fluid retention.  \n :orange[Importance]  \n - Heart failure is a chronic condition that requires lifelong management with medications (diuretics, ACE inhibitors), dietary changes (low-sodium diet), and exercise.  \n - Monitoring symptoms and regular check-ups are essential to prevent complications and hospitalizations.  \n -  Advanced heart failure may require interventions like heart transplant or mechanical circulatory support (ventricular assist devices).  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "cholesterol" : """ :orange[Cholestrol]  \n : Cholesterol is a fatty substance essential for cell function, transported in the blood by lipoproteins.  :orange[Important]  \n - High levels of low-density lipoprotein (LDL) cholesterol contribute to atherosclerosis and heart disease.  \n - Monitoring cholesterol levels (LDL, HDL, triglycerides) and maintaining a healthy diet (low in saturated fats, trans fats) are crucial for heart health.  \n - Statin medications are commonly prescribed to lower LDL cholesterol and reduce cardiovascular risk.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",


            "stroke" : """ :orange[Stroke (Cerebrovascular Accident)]  \n  A stroke occurs when blood flow to part of the brain is interrupted or reduced, leading to brain cell damage and potentially permanent neurological deficits.  \n :orange[Importance]  \n - Ischemic stroke (caused by a blocked artery) and hemorrhagic stroke (caused by a burst blood vessel) require immediate medical attention.  \n - Stroke prevention includes controlling hypertension, managing diabetes, and adopting a heart-healthy lifestyle.  \n - Rehabilitation and recovery focus on physical therapy, speech therapy, and lifestyle modifications.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "peripheral artery disease" : """ :orange[Peripheral Artery Disease (PAD)]  \n PAD is a circulatory condition where narrowed arteries reduce blood flow to the limbs, typically the legs.  \n :orange[Symptoms]  \n - Leg pain (claudication) during walking or exercise, relieved by rest.  \n - Coldness or numbness in the legs or feet.  \n - Slow-healing wounds or ulcers on the feet or toes.  \n :orange[Importance]  \n - PAD is often associated with coronary artery disease and increases the risk of heart attack and stroke.  \n - Treatment includes lifestyle changes (exercise, smoking cessation), medications (antiplatelets, statins), and in severe cases, angioplasty or surgery.  \n - Regular foot care and monitoring are essential to prevent complications like infections or gangrene.
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "systolic/diastolic blood pressure" : """:orange[Systolic/Diastolic Blood Pressure]  \n  Systolic blood pressure (top number) represents the pressure in arteries when the heart beats; diastolic blood pressure (bottom number) represents the pressure when the heart rests between beats.  \n :orange[Importance]  \n -  Blood pressure readings indicate the force of blood against artery walls and are essential for cardiovascular health assessment.  \n - Elevated systolic or diastolic blood pressure increases the risk of heart disease, stroke, and kidney disease.  \n -Regular blood pressure monitoring and lifestyle modifications (diet, exercise) are key components of hypertension management.  \n
             Enter the name of a term from the HeartPedia  to know more about it.""",


            "systolic blood pressure" : """:orange[Systolic/Diastolic Blood Pressure]  \n  Systolic blood pressure (top number) represents the pressure in arteries when the heart beats; diastolic blood pressure (bottom number) represents the pressure when the heart rests between beats.  \n :orange[Importance]  \n -  Blood pressure readings indicate the force of blood against artery walls and are essential for cardiovascular health assessment.  \n - Elevated systolic or diastolic blood pressure increases the risk of heart disease, stroke, and kidney disease.  \n -Regular blood pressure monitoring and lifestyle modifications (diet, exercise) are key components of hypertension management.  \n
             Enter the name of a term from the HeartPedia  to know more about it.""",

            "diastolic blood pressure" : """:orange[Systolic/Diastolic Blood Pressure]  \n  Systolic blood pressure (top number) represents the pressure in arteries when the heart beats; diastolic blood pressure (bottom number) represents the pressure when the heart rests between beats.  \n :orange[Importance]  \n -  Blood pressure readings indicate the force of blood against artery walls and are essential for cardiovascular health assessment.  \n - Elevated systolic or diastolic blood pressure increases the risk of heart disease, stroke, and kidney disease.  \n -Regular blood pressure monitoring and lifestyle modifications (diet, exercise) are key components of hypertension management.  \n
             Enter the name of a term from the HeartPedia  to know more about it.""",


            "holter monitor":""":orange[Holter Monitor]  \n A Holter monitor is a portable device worn to continuously record the heart's electrical activity (ECG) over 24-48 hours.  /n :orange[importance]  \n -Holter monitors detect intermittent arrhythmias that may not be captured during a standard ECG.  \n - Used to diagnose palpitations, evaluate symptoms like dizziness or fainting, and monitor response to anti-arrhythmic medications.  \n -Provides valuable data for treatment decisions and arrhythmia management strategies.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",



            "pacemaker" : """:orange[Pacemaker]  \n A pacemaker is a small device implanted under the skin to regulate abnormal heart rhythms (arrhythmias) and maintain a steady heartbeat.  \n :orange[Importance]  \n - Pacemakers monitor heart rate and deliver electrical impulses to stimulate the heart when necessary.  \n - Used to treat bradycardia (slow heart rate) or certain arrhythmias that can cause symptoms like dizziness or fainting.  \n -  Pacemaker checks and programming adjustments are performed regularly by healthcare providers.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "angina pectoris" :""":orange[Angina Pectoris]  \n Angina is chest pain or discomfort caused by reduced blood flow to the heart muscle.  \n :orange[Symptoms]  \n - Pressure, tightness, or burning sensation in the chest, often triggered by physical exertion or stress.  \n - Pain may radiate to the neck, jaw, shoulders, or arms.  \n - Symptoms typically subside with rest or nitroglycerin.  \n  :orange[Importance]  \n - Stable angina indicates underlying coronary artery disease, while unstable angina may precede a heart attack.  \n - Treatment involves lifestyle changes (smoking cessation, stress management), medications (nitroglycerin, beta-blockers), and interventions (angioplasty, stenting).  \n - Prompt medical attention is needed for worsening or new-onset angina symptoms.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "atherosclerosis" : """Atherosclerosis is the buildup of fatty deposits (plaque) within the arteries, leading to narrowing and hardening of the arteries.  \n :orange[Importance]  \n - Atherosclerosis contributes to coronary artery disease, peripheral artery disease, and stroke.  \n -Risk factors include high cholesterol, high blood pressure, smoking, diabetes, and family history.  \n Prevention involves lifestyle changes (healthy diet, exercise), medications (statins, blood thinners), and management of underlying conditions.  \n
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "electrocardiogram (ecg)": """An electrocardiogram (ECG or EKG) is a test that records the electrical activity of the heart over a period, typically displayed as a graph of voltage versus time.  \n :orange[Importance]  \n - ECGs help diagnose heart rhythm abnormalities (arrhythmias), conduction disorders, and signs of heart attack or ischemia.  \n - Used routinely in medical settings for initial cardiac assessments and ongoing monitoring of heart health.  \n - Provides valuable information for treatment decisions and management of various heart conditions.
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "ecg": """An electrocardiogram (ECG or EKG) is a test that records the electrical activity of the heart over a period, typically displayed as a graph of voltage versus time.  \n :orange[Importance]  \n - ECGs help diagnose heart rhythm abnormalities (arrhythmias), conduction disorders, and signs of heart attack or ischemia.  \n - Used routinely in medical settings for initial cardiac assessments and ongoing monitoring of heart health.  \n - Provides valuable information for treatment decisions and management of various heart conditions.
            Enter the name of a term from the HeartPedia  to know more about it.""",

            "stent" : """ :orange[Stent]  \n : A stent is a small mesh tube inserted into a blocked or narrowed artery to improve blood flow  \n :orange[Importance]  \n - Stents are commonly used in coronary artery disease to reopen blocked arteries during angioplasty.  \n -  Drug-eluting stents release medication to prevent re-narrowing (restenosis) of the artery. \n - Stents may also be used in peripheral artery disease and other vascular conditions to relieve symptoms and prevent complications.  \n 
            Enter the name of a term from the HeartPedia  to know more about it."""


            # Add more festivals and their information here
        }

        user_input_lower = user_input.lower()

        for fest, info in pedia_info.items():
            if fest == user_input_lower:
                return info

        return "I'm sorry, I'm not sure which fest you're asking about. Can you please provide more details?"

    

    if "fest_messages" not in st.session_state:
        st.session_state.fest_messages = [{"role": "assistant", "content": "Discover important heart-related terms and their meanings with our chatbot!"}]

    for message in st.session_state.fest_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Enter the Term name"):
        st.session_state.fest_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        response = get_pedia_info(prompt)

        with st.spinner(text="Thinking..."):
            st.session_state.fest_messages.append({"role": "assistant", "content": response})
            with st.chat_message("assistant"):
                st.write(response, unsafe_allow_html=True)

if __name__ == "__main__":
    app()

