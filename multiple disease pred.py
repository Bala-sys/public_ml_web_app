# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:06:12 2024

@author: Hp
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model = pickle.load(open('C:/Users/Hp/OneDrive/Desktop/Multiple disease pediction system/sav models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/Hp/OneDrive/Desktop/Multiple disease pediction system/sav models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('C:/Users/Hp/OneDrive/Desktop/Multiple disease pediction system/sav models/parkinsons_model.sav','rb'))


with st.sidebar:
    
    selected =option_menu('multiple disease prediction system',
                          ['diabetes prediction',
                           'heart disease prediction',
                           'parkinsons prediction'],
                          
                          icons = ['activity','heart','person'],
                          default_index=0)
    
if (selected == 'diabetes prediction'):
    
    st.title('diabetes prediction using ML')
    
    col1,col2,col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('BloodPressure value')
      
    with col1:
        SkinThickness = st.text_input('SkinThickness value')
        
    with col2:
        Insulin = st.text_input('Insulin level')
        
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
        
    with col2:
        Age = st.text_input('Age of Person')
        
    
    diab_diagnosis = ''
    
    if st.button ('Diabetes test result'):
        diab_pediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_pediction[0]==1):
            diab_diagnosis = 'The person is Diabetic'
            
        else:
            diab_diagnosis = 'The person is Not Diabetic'
            
    st.success(diab_diagnosis)
if (selected == 'heart disease prediction'):
    
    st.title('heart disease prediction using ML')
    
if (selected == 'parkinsons prediction'):
    
    st.title('parkinsons prediction using ML')







