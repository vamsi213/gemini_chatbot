import streamlit as st
import google.generativeai as genai

st.title("Gemini AI Chatbot")

f = open("E:\gemini_chatbot\keys\.gemimi_api_key.txt")
key = f.read()

genai.configure(api_key=key)




model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              system_instruction="""You are an AI Assistant who resolves any
                                  Queries of the user.Your name is Pikachu.""")


if "memory" not in st.session_state:
    st.session_state["memory"] = []
    
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.chat_message("ai").write("Hi, How may i help you?")

chat = model.start_chat(history=st.session_state["chat_history"])

for msg in chat.history:
    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt = st.chat_input()

if user_prompt:
    # Add user input to memory
    st.session_state["memory"].append(user_prompt)
    st.chat_message("user").write(user_prompt)

    # Send user input to chat model and get response
    response = chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)

    # Update chat history in session state
    st.session_state["chat_history"] = chat.history

   