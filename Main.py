# streamlit_app.py
import streamlit as st
import ModelScript  # File which contain Machine Learning Model


st.title("Symptoms Analyzer")
st.header("How are you feeling?")

# Symptoms dropdown
symptoms_list = ['Fever',
 'Chills',
 'Headache',
 'Joint Pain',
 'Nausea',
 'Vomiting',
 'Cough',
 'Fatigue',
 'Chest Pain',
 'Short Breath',
 'Sweating',
 'Thirst',
 'Hunger',
 'Frequent Urine',
 'Blurred Vision',
 'Yellow Eyes',
 'Itchy Skin',]
symptom1 = st.selectbox("Symptom 1", symptoms_list)
symptom2 = st.selectbox("Symptom 2", symptoms_list)
symptom3 = st.selectbox("Symptom 3", symptoms_list)
symptom4 = st.selectbox("Symptom 4", symptoms_list)
symptom5 = st.selectbox("Symptom 5", symptoms_list)


selected_symptoms = [symptom1, symptom2, symptom3, symptom4, symptom5]


symptoms_array = [1 if symptom in selected_symptoms else 0 for symptom in symptoms_list]


# Sliders for Weight, Age, and Heart Rate
weight = st.slider("Weight (In KG)", 30, 200)  # Weight range from 30 to 200 for example
age = st.slider("Age", 1, 100)  # Age range from 1 to 100
heart_rate = st.slider("Heart Rate", 50, 180)  # Assuming heart rate range from 50 to 180


symptoms_array.extend([weight, age, heart_rate])

symptoms_list_2d = [symptoms_array]


# Predict button
if st.button("Predict"):
    # Here, you should call your model prediction function from script.py
    # For this example, I'm just assuming a dummy function `predict_disease` in your script.py
    result = ModelScript.prediction(symptoms_list_2d)
    st.write(f"You most probably have: {result}")

# Sidebar for image (optional if you want to showcase something)
st.write("\n\n\n")  
st.sidebar.image("https://cdn4.iconfinder.com/data/icons/health-1-0/512/0112healthvirus1_DEF.png", use_column_width=True)

