# InsightAI 🧠
An intelligent document-aware chatbot built with OpenAI, Streamlit, and Python.

## 🚀 Overview
InsightAI lets users upload documents (PDF, Word, Excel, CSV) and chat with an AI assistant that can:
- Automatically summarize uploaded files
- Answer questions based on the document
- Flag sensitive content
- Log and store chat history
- Let users resume, rename, pin ⭐, or delete 🗑 previous chats

---

## 🛠 Features
- 📄 File upload (PDF, DOCX, XLSX, CSV)
- 🧠 GPT-4 powered natural language responses
- 📝 Real-time document summarization
- 💬 Interactive chat UI with Streamlit
- ⭐ Pin, 🗑 Delete, and 🔁 Resume chat sessions
- 💾 Optional persistent storage via SQLite
- 🛡 Moderation using OpenAI's safety layer
- 🔍 Keyword logging and content tagging

---

## ⚙️ Technologies Used
- Python 3.11+
- [Streamlit](https://streamlit.io/)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
- SQLite for future session persistence
- `python-dotenv`, `requests`, and more (see `requirements.txt`)

---

## 📦 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/TroyJLorents-GH/InsightAI.git
cd InsightAI
---

```bash
### 2. Set Up Environment
python -m venv .venv
.venv\\Scripts\\activate    # Windows

---

```bash
### 3. Install Dependencies
pip install -r requirements.txt

---

```bash
### 4 Add Your API Key
Create a .env file:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx

---

```bash
### 5. Run the app
streamlit run streamlit_app.py

---
License
MIT License — feel free to fork and build upon it

---
Created by
Troy Lorents | @TroyJLorents-GH

