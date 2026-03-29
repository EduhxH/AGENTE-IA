<div align="center">

<img src="https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
<img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
<img src="https://img.shields.io/badge/ChromaDB-VectorDB-7C3AED?style=for-the-badge" />
<img src="https://img.shields.io/badge/Ollama-Local%20LLM-000000?style=for-the-badge" />
<img src="https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white" />
<img src="https://img.shields.io/badge/status-in%20development-yellow?style=for-the-badge" />

<br/>
<br/>

# 🧠 Local AI Agent with RAG

**A document-aware AI agent running 100% locally.**  
No cloud. No shortcuts. Just engineering.

> ⚠️ **Note:** The source code, comments and variable names are written in **Portuguese (pt-BR)**, as this project was developed for study purposes in a Brazilian/Portuguese context.

[How It Works](#-how-it-works) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Getting Started](#-getting-started) • [Project Structure](#-project-structure)

</div>

---

## 🧩 About the Project

This project is a hands-on laboratory for exploring local LLMs and the **RAG (Retrieval-Augmented Generation)** pattern.

The goal was to build a chat that doesn't respond by guessing — but by consulting a knowledge base built from real documents.

Everything runs locally, making it possible to understand each step of the pipeline:

- PDF ingestion and upload via UI
- Semantic chunking and vectorization
- Similarity-based retrieval with relevance threshold
- Context-aware response generation with anti-hallucination prompt
- Persistent memory across sessions

---

## ⚡ How It Works

```
User question
     ↓
Semantic search in ChromaDB (with relevance threshold)
     ↓
Relevant chunks become the prompt context
     ↓
llama3.2 (via Ollama) generates the response (system prompt enforced)
     ↓
Answer streamed in real time to the UI
```

---

## ✨ Features

- 🔍 **Semantic chunking** — uses `SemanticChunker` to split documents by meaning, not character count
- 📄 **Context-aware responses** — system prompt enforces answers based strictly on document content
- 🚫 **Anti-hallucination** — relevance threshold filters out irrelevant chunks before generation
- 📤 **PDF upload via UI** — drag and drop PDFs directly in the sidebar, indexed automatically
- 🧠 **Persistent memory** — conversation history saved across sessions as JSON
- ⚙️ **Model parameter tuning** — adjust temperature, top-p, top-k and context window via sidebar
- 📊 **Embedding dashboard** — PCA 2D visualization of all indexed chunks
- 🔁 **Incremental indexing** — MD5-based deduplication prevents re-indexing existing documents
- 💬 **Chat with history** — last N turns included as conversational context
- ⚡ **Response streaming** — token-by-token output for a natural feel
- 🐳 **Dockerized** — runs fully containerized with persistent volumes
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
| [scikit-learn](https://scikit-learn.org/) | PCA for embedding visualization |
| [Docker](https://www.docker.com/) | Containerization |

---

## 📦 Prerequisites

- [Python 3.13+](https://www.python.org/)
- [Ollama](https://ollama.com/) installed and running locally
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (optional, for containerized run)

---

## 🚀 Getting Started

### 1. Pull the required models

```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 2. Clone the repository and set up environment

```bash
git clone https://github.com/EduhxH/AGENTE-IA.git
cd AGENTE-IA
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
```

### 3. Configure environment variables

Edit `RAG/.env`:

```env
OLLAMA_BASE_URL=http://localhost:11434
```

### 4. Build the vector database

```bash
python RAG/criar_db.py
```

### 5. Run the app

```bash
streamlit run RAG/app.py
```

> ✅ App running at `http://localhost:8501`

---

### 🐳 Running with Docker

```bash
docker-compose up --build
```

> The `chroma_db`, `memory_db` and `base` folders are mounted as volumes — data persists across container rebuilds.

---

## 📁 Project Structure

```
RAG1/
│
├── RAG/
│   ├── base/               # Source documents (PDFs)
│   ├── chroma_db/          # Persisted vector database
│   ├── memory_db/          # Persisted conversation history
│   │
│   ├── app.py              # Streamlit interface & chat logic
│   ├── criar_db.py         # PDF ingestion & vectorization script
│   ├── memory.py           # Persistent memory module
│   └── .env                # Environment variables
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## ⚠️ Common Issues

**Vector database not found or malformed**

```bash
Remove-Item -Recurse -Force RAG\chroma_db   # Windows
python RAG/criar_db.py
```

**Ollama connection error**

Make sure Ollama is running and the port in `.env` matches:

```bash
curl http://localhost:11434   # should return "Ollama is running"
```

**Retrieval returns no results**

The default relevance threshold is `0.2`. If your document scores lower, adjust in `app.py`:

```python
THRESHOLD = 0.1
```

---

## 🧠 What I Learned

- How to build a full RAG pipeline from scratch
- The difference between fixed chunking and semantic chunking
- How relevance thresholds prevent hallucination from irrelevant context
- How vector databases store and retrieve semantic information
- How to run open-source LLMs locally with Ollama
- How to orchestrate AI pipelines with LangChain
- How to containerize a Python AI application with Docker

---

## 🔮 Future Improvements

- [x] PDF upload through the UI
- [x] Persistent memory across sessions
- [x] Model parameter tuning via interface
- [x] Dockerization
- [x] Embedding visualization dashboard

---

<div align="center">

Made with 💜 by [EduhxH](https://github.com/EduhxH)

</div>
