import streamlit as st
import joblib

model = joblib.load('model.joblib')

st.title('News Classifier App')

news =[]
news_text = st.text_area(height=180 , placeholder='Enter news here',label="")
news.append(news_text)

if st.button("Predict"):
    prediction = model.predict(news)
    st.success(f"Predicted category : {prediction[0]}")