"""
Created on sat october 22 11:21:51 2022

@author: Navin"""

import pickle
import streamlit as st



# loading the saved models

insurance_model = pickle.load(open('insurance.sav','rb'))

# page title
st.title('INSURANCE PRICE PREDICTION USING ML')

    # code for Prediction
 
col1, col2  = st.columns(2)

with col1:
      age = st.text_input('Age')
        
with col2:
        sex = st.text_input('Sex(0 if female, 1 if male)')
        
with col1:
        bmi = st.text_input('BMI(Any float values)')
        
with col2:
        child = st.text_input('Children (only integers)')
        
with col1:
        smoker = st.text_input('Smoker (0 if non-smoker else 1)')
        
with col2:
        nwest = st.text_input('region_northwest(type 0 or 1)')

with col1:
        seast = st.text_input('region_southeast(type 0 or 1)')
        
with col2:
        swest = st.text_input('region_southwest(type 0 or 1)')
        
        
    
if st.button('Compute Price'):
    
    insu_pred = insurance_model.predict([[age,sex,bmi,child,smoker,nwest,seast,swest]])
    st.success(f"The predicted price is {insu_pred[0]}")
    