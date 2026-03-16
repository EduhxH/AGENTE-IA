import streamlit as st
import os
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama

st.set_page_config(page_title="Agente IA", layout="centered")
st.title("Agente IA")

PASTA_DB = "RAG/chroma_db"

def carregar_sistema():
    modelo_vetores = OllamaEmbeddings(model="nomic-embed-text")
    banco = Chroma(persist_directory=PASTA_DB, embedding_function=modelo_vetores)
    ia = ChatOllama(model="llama3.2", temperature=0)
    return banco, ia

if not os.path.exists(PASTA_DB):
    st.error("Erro: Banco de dados não encontrado.")
    st.stop()

banco, ia = carregar_sistema()

if "historico" not in st.session_state:
    st.session_state.historico = []

for conversa in st.session_state.historico:
    with st.chat_message(conversa["autor"]):
        st.write(conversa["texto"])

if pergunta := st.chat_input("Escreva aqui..."):
    st.session_state.historico.append({"autor": "user", "texto": pergunta})
    with st.chat_message("user"):
        st.write(pergunta)

    with st.chat_message("assistant"):
        busca = banco.similarity_search(pergunta, k=3)
        contexto = "\n".join([doc.page_content for doc in busca])
        
        prompt = f"Contexto:\n{contexto}\n\nPergunta: {pergunta}"
        
        resposta_final = ""
        placeholder = st.empty()
        
        for pedaco in ia.stream(prompt):
            resposta_final += pedaco.content
            placeholder.write(resposta_final)
            
    st.session_state.historico.append({"autor": "assistant", "texto": resposta_final})