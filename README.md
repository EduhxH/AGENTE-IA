# 🧠 Agente de IA Local com RAG

![Python](https://img.shields.io/badge/Python-3.13.12+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![ChromaDB](https://img.shields.io/badge/Chroma-VectorDB-purple)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-black)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

> Um agente de IA com memória baseada em documentos, rodando 100% local. Sem nuvem. Sem atalhos. Só engenharia.

---

## 🧩 Sobre o Projeto

Este projeto é um laboratório prático para explorar LLMs locais e o padrão RAG (Retrieval-Augmented Generation).

A ideia foi criar um chat que não responde por adivinhação, mas sim consultando uma base de conhecimento construída a partir de documentos reais.

Tudo roda localmente, permitindo entender cada etapa:

- Ingestão de PDFs  
- Vetorização de texto  
- Busca semântica  
- Geração de resposta com contexto  

---

## ⚡ Como Funciona

1. O utilizador faz uma pergunta  
2. O sistema busca trechos relevantes no ChromaDB  
3. Esses trechos viram o contexto do prompt  
4. O modelo llama3.2 (via Ollama) gera a resposta  
5. A resposta é exibida em tempo real (streaming)  

---

## ✨ Funcionalidades

- Busca semântica inteligente  
- Respostas com contexto real  
- Chat com histórico  
- Streaming de resposta  
- Execução 100% local  

---

## 🛠️ Stack Tecnológica

- Streamlit (interface)  
- LangChain (pipeline RAG)  
- ChromaDB (base vetorial)  
- Ollama  
  - llama3.2 (LLM)  
  - nomic-embed-text (embeddings)  

---

## 📁 Estrutura do Projeto

RAG/
│
├── base/
├── chroma_db/
│
├── gabarito/
│ ├── app.py
│ ├── criar_db.py
│ └── .env
│
└── requirements.txt

---

## ⚙️ Como Executar

### 1. Instalar Ollama + modelos

ollama pull llama3.2
ollama pull nomic-embed-text

## 2. Instalar dependências

pip install -r requirements.txt

## 3. Criar a base vetorial

python criar_db.py

## 4. Executar o app

cd RAG/gabarito
streamlit run app.py

## ⚠️ Problemas Comuns
## Banco não encontrado

Verifique se existe:
RAG/chroma_db
Caso não exista:
python criar_db.py

Streamlit não encontra o app:
Execute:
cd RAG/gabarito
streamlit run app.py

## 🧪 Melhorias Futuras

Upload de PDFs pela interface
Memória persistente
Ajuste de parâmetros do modelo
Docker
Visualização de embeddings

## 🎯 Aprendizados

Integração entre dados e LLM
Diferença entre LLM puro e RAG
Construção de sistemas de IA locais
