
import streamlit as st
import nltk
from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


chatbot=pipeline("text-generation", model="distilgpt2") #distilgpt2 is the pre-trained model going to use  #pipeline used for hugging face model

def healthcare_chatbot(user_input):
    # Preprocess the user input
    if "sympton" in user_input:
       return "Please Consult Doctor for accurate advice"
    elif "appointment" in user_input:
        return "Please contact your doctor's office to schedule an appointment"
    elif "medication" in user_input:
        return "Please consult your doctor before taking any medication"
    else:
        response =chatbot(user_input,max_length=500,num_return_sequences=1) #max_lenght =including text from the user and the answer , num_return_sequence = no of answer from the prompt
        return response[0]['generated_text']

#Streamlit web interface 
def main():
    st.title("AI HealthCare Assistant Chatbot")
    user_input=st.text_input("How can I assist you today?")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            with st.spinner("Processing your query,Please Wait ..."):
                response=healthcare_chatbot(user_input)
            st.write("AI Healthcare Assistant :",response)
            print(response)
        else:
            st.write("Please enter a message to get a response.")
main()  
