# InsightAI 🧠
An intelligent document-aware chatbot built with OpenAI, Streamlit, and Python for demo project.

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
```

### 2. Set Up Environment
```bash
python -m venv .venv
.venv\\Scripts\\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4 Add Your API Key
- Create a .env file:
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the app
```bash
streamlit run streamlit_app.py
```


Created by
Troy Lorents | @TroyJLorents-GH

