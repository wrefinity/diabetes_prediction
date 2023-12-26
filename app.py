import pickle
import streamlit as st
from streamlit_option_menu import option_menu



# loading the  model
with open('./model/db_model.pkl', 'rb') as file:
    db_model = pickle.load(file)

# title
st.title("DIABETES DISEASE PREDICTION USING PIMA DATASET")
# sidebar for navigation
with st.sidebar:
    selected = option_menu('Diabetes Disease Prediction System',   
                          ['Diabetes Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('patient age')
        
    with col2:
        urea = st.text_input('patient urea')
    
    with col3:
        cr = st.text_input('creatinine level.')
    
    with col1:
        hbA1c = st.text_input('hemoglobin A1c level.')
    
    with col2:
        chol = st.text_input('Cholesterol level')
    
    with col3:
        tg = st.text_input('Triglyceride level')
    
    with col1:
        hdl = st.text_input('High-density lipoprotein (HDL) cholesterol level ')
    
    with col2:
        ldl = st.text_input('Low-Density Lipoprotein (LDL) cholesterol level ')

    with col3:
        vldl = st.text_input('Patient very low-density lipoprotein (VLDL) cholesterol level ')
    
    with col1:
        bmi = st.text_input('enter patient body mass index level ')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        age = float(age)
        urea = float(urea)
        cr = float(cr)
        hbA1c = float(hbA1c)
        chol = float(chol)
        tg = float(tg)
        hdl = float(hdl)
        ldl = float(ldl)
        vldl = float(vldl)
        bmi = float(bmi)
        d_pred = db_model.predict([
            [age, urea, cr, hbA1c, chol, tg, hdl, ldl, vldl, bmi]
        ])
        
        if (d_pred[0] == 1):
          d_diagnosis = 'The person is diabetic'
        elif (d_pred[0] == 0):
          d_diagnosis = 'The person is not diabetic'
        else:
            d_diagnosis = 'The person is partially diabetic'
        
        st.success(d_diagnosis)
