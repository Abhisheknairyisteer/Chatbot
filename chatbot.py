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
st.write("response from the chatbot.")

# Input box for the user's question
question = st.text_input("You:", "")

# Button to send the question   
if st.button("Send"):
    if question.strip():
        response = chat.send_message(question)
        st.write("Bot:", response.text)
    else:
        st.write("Please enter a question.")