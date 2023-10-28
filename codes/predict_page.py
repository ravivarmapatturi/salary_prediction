import streamlit as st
import joblib
import numpy as np



def load_model():
    model=joblib.load(r"C:\Users\raviv\OneDrive\Documents\learning\ml\salary_prediction\models\best_model.pkl")
    le_country=joblib.load(r"C:\Users\raviv\OneDrive\Documents\learning\ml\salary_prediction\codes\le_country.pkl")
    le_education=joblib.load(r"C:\Users\raviv\OneDrive\Documents\learning\ml\salary_prediction\codes\le_education.pkl")
    return model,le_country,le_education

model,le_country,le_education=load_model()
regressor=model



def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("""### We need some information to predict the salary""")
    
    countries=('United States of America',
       'United Kingdom of Great Britain and Northern Ireland',
       'Australia', 'Netherlands', 'Germany', 'Sweden', 'France', 'Spain',
       'Brazil', 'Italy', 'Canada', 'Switzerland', 'India', 'Austria',
       'Poland', 'Denmark')
    
    education=('Bachelor’s', 'others', 'Master’s', 'Professional degree')
    
    country=st.selectbox("country",countries)
    education=st.selectbox("education",education)
    experience=st.slider("experience",0,50,2)
    
    ok=st.button("Calculate Salary")
    if ok:
        X=np.array([[country,education,experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        
        salary=regressor.predict(X)
        st.subheader(f" The estimated salary is ${salary[0]:.2f}")
    