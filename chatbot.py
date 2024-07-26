import streamlit as st
import google.generativeai as genai

# Configure the API key for Google Generative AI
API_KEY = "AIzaSyAIr7m1lYDleEVKdCnSXAZrWAD15MuhKVw"
genai.configure(api_key=API_KEY)

# Initialize the Generative Model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Streamlit UI
st.title("Chatbot")
st.write("answer from chatbot.")

# Input box for the user's question
question = st.text_input("Me:", "")

# Button to send the question   
if st.button("sned to my chatbot"):
    if question.strip():
        response = chat.send_message(question)
        st.write("AI:", response.text)
    else:
        st.write("Please enter a question.")