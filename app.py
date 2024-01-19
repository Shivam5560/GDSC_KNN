import streamlit as st
import pickle
import time



st.title('Diabetes Prediction using KNN (DEMO)')
with st.sidebar:
    st.write('Here you can write info about Knn and Your project ')
#Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age

col1,col2 = st.columns(2)
with col1:
    a = st.number_input('Pregnancies')
    b = st.number_input('Glucose level')
    c = st.number_input('Blood Pressure')
    d = st.number_input('Skin Thickness')
with col2:
    e = st.number_input('Insulin')
    f = st.number_input('BMI')
    g = st.number_input('Diabetes Pedigree Function')
    h = st.number_input('Age')
sub = st.button('Submit')
if sub:
    with st.spinner('Wait'):
        time.sleep(1)
        with open('model.pkl','rb') as file:
            inputs = [[a,b,c,d,e,f,g,h]]
            print(inputs)
            model = pickle.load(file)
            prediction = model.predict(inputs)
            if prediction == 0:
                st.balloons()
                st.text_area(label='Outcome',value='No Diabetes Risk')
            else:
                st.text_area(label='Outcome',value='High Risk of Diabetes')

