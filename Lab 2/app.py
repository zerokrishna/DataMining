import streamlit as st
import joblib

model = joblib.load('model.joblib')

st.title('Iris flower Classifier')

sepal_length = st.number_input("Enter Sepal length in cm")
sepal_width = st.number_input("Enter Sepal width in cm")
petal_length = st.number_input("Enter Petal length in cm ")
petal_width = st.number_input("Enter Petal width in cm")

sample = [[sepal_length,sepal_width,petal_length,petal_width]]

if st.button("Predict"):
    predection = model.predict(sample)
    st.success(f"Predicted Species:{predection[0]}")