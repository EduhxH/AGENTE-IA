<div align="center">

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/ChromaDB-VectorDB-7C3AED?style=for-the-badge" />
<img src="https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge" />
<img src="https://img.shields.io/badge/status-in%20development-yellow?style=for-the-badge" />

<br/>
<br/>

# 🧠 Local AI Agent with RAG

**A document-aware AI agent running 100% locally.**  
No cloud. No shortcuts. Just engineering.

> ⚠️ **Note:** The source code, comments and variable names are written in **Portuguese (pt-BR)**, as this project was developed for study purposes in a Brazilian context.

[How It Works](#-how-it-works) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Project Structure](#-project-structure)

</div>

---

## 🧩 About the Project

This project is a hands-on laboratory for exploring local LLMs and the **RAG (Retrieval-Augmented Generation)** pattern.

The goal was to build a chat that doesn't respond by guessing — but by consulting a knowledge base built from real documents.

Everything runs locally, making it possible to understand each step of the pipeline:

- PDF ingestion
- Text vectorization
- Semantic search
- Context-aware response generation

---

## ⚡ How It Works

```
User question
     ↓
Semantic search in ChromaDB
     ↓
Relevant chunks become the prompt context
     ↓
llama3.2 (via Ollama) generates the response
     ↓
Answer streamed in real time to the UI
```

---

## ✨ Features

- 🔍 **Intelligent semantic search** — finds the most relevant document chunks for each query
- 📄 **Context-aware responses** — the model answers based on real document content, not hallucinations
- 💬 **Chat with history** — conversation memory across turns
- ⚡ **Response streaming** — token-by-token output for a natural feel
- 🔒 **100% local execution** — no API keys, no cloud, full privacy

---

## 🛠 Tech Stack

| Technology | Role |
|---|---|
| [Streamlit](https://streamlit.io/) | Web interface |
| [LangChain](https://www.langchain.com/) | RAG pipeline orchestration |
| [ChromaDB](https://www.trychroma.com/) | Vector database |
| [Ollama](https://ollama.com/) — `llama3.2` | Local LLM for generation |
| [Ollama](https://ollama.com/) — `nomic-embed-text` | Local embeddings model |

---

## 📦 Prerequisites

- [Python 3.13+](https://www.python.org/)
- [Ollama](https://ollama.com/) installed and running locally

---

## 🚀 Getting Started

### 1. Pull the required models

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Build the vector database

```bash
python criar_db.py
```

### 4. Run the app

```bash
cd RAG/gabarito
streamlit run app.py
```

> ✅ App running at `http://localhost:8501`

---

## 📁 Project Structure

```
RAG/
│
├── base/                   # Source documents (PDFs)
├── chroma_db/              # Persisted vector database
│
├── gabarito/
│   ├── app.py              # Streamlit interface & chat logic
│   ├── criar_db.py         # PDF ingestion & vectorization script
│   └── .env                # Environment variables
│
└── requirements.txt
```

---

## ⚠️ Common Issues

**Vector database not found**

If you see an error about a missing database, make sure the `chroma_db/` folder exists:

```bash
python criar_db.py
```

**Streamlit can't find the app**

Always run from the correct directory:

```bash
cd RAG/gabarito
streamlit run app.py
```

---

## 🧠 What I Learned

- How to build a full RAG pipeline from scratch
- The difference between a pure LLM and a retrieval-augmented system
- How vector databases store and retrieve semantic information
- How to run open-source LLMs locally with Ollama
- How to orchestrate AI pipelines with LangChain

---

## 🔮 Future Improvements

- [ ] PDF upload through the UI
- [ ] Persistent memory across sessions
- [ ] Model parameter tuning via interface
- [ ] Dockerization
- [ ] Embedding visualization dashboard

---

<div align="center">

Made with 💜 by [EduhxH](https://github.com/EduhxH)

</div>
