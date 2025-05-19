import streamlit as st
import openai
import os
import sqlite3
from dotenv import load_dotenv
from file_uploader import extract_text

# Load environment variable
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY") or st.secrets.get("OPENAI_API_KEY")

st.set_page_config(page_title="Insight AI", page_icon="🧠")
st.title("Insight AI 🧠")

DB_PATH = "db/chatbot.db"

if "messages" not in st.session_state:
    st.session_state.messages = []
if "doc_text" not in st.session_state:
    st.session_state.doc_text = ""
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "chat_titles" not in st.session_state:
    st.session_state.chat_titles = []

# Function to fetch keywords from db for a given user input
def get_keywords_for_prompt(prompt):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT keywords FROM chatlog WHERE user_input = ? ORDER BY timestamp ASC LIMIT 1", (prompt,))
    row = cursor.fetchone()
    conn.close()
    if row and row[0]:
        return " · ".join(row[0].split(", "))
    return "Untitled"

# Function to query OpenAI chat model
def ask_openai(prompt, model="o3"):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error from OpenAI: {e}"

# Sidebar: chat history + new chat
st.sidebar.title("📃 Chat History")
if st.sidebar.button("Start New Chat"):
    if st.session_state.messages:
        st.session_state.chat_history.append(st.session_state.messages)
        first_user_input = next((msg["content"] for msg in st.session_state.messages if msg["role"] == "user"), "")
        title = get_keywords_for_prompt(first_user_input)
        st.session_state.chat_titles.append(title)
    st.session_state.messages = []
    st.session_state.doc_text = ""
    st.rerun()

if st.session_state.chat_history:
    to_delete = None
    for i, chat in enumerate(st.session_state.chat_history[::-1], 1):
        title_index = len(st.session_state.chat_history) - i
        with st.sidebar.expander(f"{st.session_state.chat_titles[title_index]}", expanded=False):
            new_title = st.text_input(f"Rename Chat #{i}", st.session_state.chat_titles[title_index], key=f"title_{i}")
            st.session_state.chat_titles[title_index] = new_title
            col1, col2 = st.columns([1, 1])
            with col1:
                if st.button(f"🔄 Resume Chat #{i}", key=f"resume_{i}"):
                    st.session_state.messages = chat
                    st.rerun()
            with col2:
                if st.button("🗑️ Delete", key=f"delete_{i}"):
                    to_delete = title_index
            for msg in chat:
                role = "You" if msg["role"] == "user" else "Bot"
                st.markdown(f"**{role}:** {msg['content']}")
    if to_delete is not None:
        del st.session_state.chat_history[to_delete]
        del st.session_state.chat_titles[to_delete]
        st.rerun()

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input with file support
prompt = st.chat_input(
    "Ask a question or upload a document...",
    accept_file=True,
    file_type=["pdf", "docx", "xlsx", "csv"]
)

if prompt is not None:
    if prompt.files:
        uploaded_file = prompt.files[0]
        doc_text = extract_text(uploaded_file)
        st.session_state.doc_text = doc_text
        st.toast("Document uploaded and text extracted!", icon="📄")

        # Step 1: Request a summary from the assistant
        summary_prompt = f"Summarize or describe this document briefly:\n\n{doc_text}"
        summary_response = ask_openai(summary_prompt)

        st.session_state.messages.append({"role": "assistant", "content": summary_response})
        with st.chat_message("assistant"):
            st.markdown(summary_response)

        # Step 2: Prompt the user to ask a question about the file
        followup_prompt = "File uploaded and text extracted. What questions do you have about the document?"
        st.session_state.messages.append({"role": "assistant", "content": followup_prompt})
        with st.chat_message("assistant"):
            st.markdown(followup_prompt)

    if prompt.text:
        user_input = prompt.text
        full_prompt = user_input

        if st.session_state.doc_text:
            full_prompt = f"Answer this based on the document below:\n\n{st.session_state.doc_text}\n\nUser question: {user_input}"

        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        ai_response = ask_openai(full_prompt)

        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.markdown(ai_response)
