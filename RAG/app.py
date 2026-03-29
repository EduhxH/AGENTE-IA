import streamlit as st
import os
import pandas as pd
import numpy as np
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
from sklearn.decomposition import PCA  # type: ignore

from memory import carregar_historico, guardar_mensagem, limpar_historico
from criar_db import carregar_pdf_bytes, dividir_texto, gerar_vetores

load_dotenv()

st.set_page_config(page_title="Agente IA", layout="wide")

PASTA_DB = os.getenv("CHROMA_PATH", "RAG/chroma_db")
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

SYSTEM_PROMPT = """Você é um assistente que responde EXCLUSIVAMENTE com base no contexto fornecido.
Se a resposta não estiver no contexto, diga: "Não encontrei essa informação no documento."
Nunca invente informações."""

THRESHOLD = 0.2
MAX_HISTORICO = 4


@st.cache_resource
def carregar_sistema(model_name: str, ollama_url: str):
    modelo_vetores = OllamaEmbeddings(model="nomic-embed-text", base_url=ollama_url)
    banco = Chroma(persist_directory=PASTA_DB, embedding_function=modelo_vetores)
    ia = ChatOllama(model=model_name, base_url=ollama_url, temperature=0)
    return banco, ia, modelo_vetores


with st.sidebar:
    st.header("Configuração do modelo")

    model_name = st.selectbox(
        "Modelo LLM",
        ["llama3.2", "llama3.1", "mistral", "phi3", "gemma2"],
        index=0
    )

    temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=0.0, step=0.05,
                            help="0 = determinístico, 1 = criativo")

    top_p = st.slider("Top-p", min_value=0.1, max_value=1.0, value=0.9, step=0.05,
                      help="Controla a diversidade do vocabulário")

    top_k = st.slider("Top-k", min_value=1, max_value=100, value=40, step=1,
                      help="Número de tokens candidatos a cada passo")

    num_ctx = st.select_slider("Context window (tokens)",
                               options=[2048, 4096, 8192, 16384],
                               value=4096)

    st.divider()

    st.header("Documentos")

    pdfs = st.file_uploader(
        "Adicionar PDFs",
        type="pdf",
        accept_multiple_files=True,
        help="Os PDFs são indexados automaticamente após o upload"
    )

    if pdfs:
        if st.button("Indexar PDFs", type="primary", use_container_width=True):
            with st.spinner("A indexar documentos..."):
                todos_chunks = []
                for pdf in pdfs:
                    try:
                        docs = carregar_pdf_bytes(pdf.name, pdf.read())
                        chunks = dividir_texto(docs)
                        todos_chunks.extend(chunks)
                    except Exception as e:
                        st.error(f"Erro ao processar '{pdf.name}': {e}")

                if todos_chunks:
                    stats = gerar_vetores(todos_chunks)
                    st.success(
                        f"{stats['novos']} chunks novos indexados. "
                        f"Total na base: {stats['total']}"
                    )
                    st.cache_resource.clear()  

    st.divider()

    st.header("Memória")

    memoria_activa = st.toggle("Memória persistente", value=True,
                               help="Guarda o histórico entre sessões")

    if st.button("Limpar histórico", use_container_width=True):
        limpar_historico()
        st.session_state.historico = []
        st.rerun()

    st.divider()

    st.header("Embeddings")

    if st.button("Visualizar embeddings", use_container_width=True):
        st.session_state.mostrar_dashboard = not st.session_state.get("mostrar_dashboard", False)


if not os.path.exists(PASTA_DB):
    st.error("Banco de dados não encontrado. Faz upload de PDFs para começar.")
    st.stop()

banco, ia, modelo_vetores = carregar_sistema(model_name, OLLAMA_URL)

ia.temperature = temperature
ia.top_p = top_p
ia.top_k = top_k
ia.num_ctx = num_ctx

if "historico" not in st.session_state:
    if memoria_activa:
        st.session_state.historico = carregar_historico()
    else:
        st.session_state.historico = []

if st.session_state.get("mostrar_dashboard", False):
    st.subheader("Dashboard de Embeddings")

    with st.spinner("A carregar embeddings..."):
        try:
            dados = banco.get(include=["embeddings", "documents", "metadatas"])
            vecs = np.array(dados["embeddings"])
            docs_text = dados["documents"]
            metas = dados["metadatas"]

            if len(vecs) < 3:
                st.warning("Precisas de pelo menos 3 chunks indexados para visualizar.")
            else:

                from sklearn.decomposition import PCA  # type: ignore

                n_components = min(3, len(vecs))
                pca = PCA(n_components=n_components)
                coords = pca.fit_transform(vecs)

                labels = [
                    m.get("doc_name", f"chunk_{i}")
                    for i, m in enumerate(metas)
                ]
                preview = [t[:60] + "..." if len(t) > 60 else t for t in docs_text]

                df = pd.DataFrame({
                    "x": coords[:, 0],
                    "y": coords[:, 1],
                    "documento": labels,
                    "preview": preview,
                    "chunk_size": [m.get("chunk_size", 0) for m in metas]
                })

                variancia = pca.explained_variance_ratio_
                col1, col2, col3 = st.columns(3)
                col1.metric("Total de chunks", len(vecs))
                col2.metric("Dimensões originais", vecs.shape[1])
                col3.metric("Variância explicada (PC1+PC2)",
                            f"{(variancia[0]+variancia[1])*100:.1f}%")

                st.scatter_chart(df, x="x", y="y", color="documento",
                                 size="chunk_size", use_container_width=True)

                with st.expander("Ver tabela de chunks"):
                    st.dataframe(df[["documento", "preview", "chunk_size"]],
                                 use_container_width=True)

        except ImportError:
            st.error("Instala scikit-learn para o dashboard: pip install scikit-learn")
        except Exception as e:
            st.error(f"Erro ao carregar embeddings: {e}")

    st.divider()

st.title("Agente IA")

for conversa in st.session_state.historico:
    with st.chat_message(conversa["autor"]):
        st.write(conversa["texto"])

if pergunta := st.chat_input("Escreva aqui..."):
    st.session_state.historico.append({"autor": "user", "texto": pergunta})
    if memoria_activa:
        guardar_mensagem("user", pergunta)

    with st.chat_message("user"):
        st.write(pergunta)

    with st.chat_message("assistant"):
    
        resultados = banco.similarity_search_with_relevance_scores(pergunta, k=5)
        chunks_relevantes = [doc for doc, score in resultados if score >= THRESHOLD]

        if not chunks_relevantes:
            resposta_final = "Não encontrei informação relevante sobre esse tema no documento."
            st.write(resposta_final)
        else:

            partes = []
            for i, doc in enumerate(chunks_relevantes, 1):
                fonte = doc.metadata.get("doc_name", doc.metadata.get("source", "desconhecido"))
                pagina = doc.metadata.get("page", "?")
                partes.append(f"[Trecho {i} — {fonte}, pág. {pagina}]\n{doc.page_content}")
            contexto = "\n\n---\n\n".join(partes)

            mensagens = [SystemMessage(content=SYSTEM_PROMPT)]
            historico_recente = st.session_state.historico[-(MAX_HISTORICO * 2):-1]
            for msg in historico_recente:
                if msg["autor"] == "user":
                    mensagens.append(HumanMessage(content=msg["texto"]))
                else:
                    mensagens.append(AIMessage(content=msg["texto"]))

            mensagens.append(
                HumanMessage(content=f"Contexto:\n{contexto}\n\nPergunta: {pergunta}")
            )

            resposta_final = ""
            placeholder = st.empty()
            for pedaco in ia.stream(mensagens):
                resposta_final += pedaco.content
                placeholder.write(resposta_final)

    st.session_state.historico.append({"autor": "assistant", "texto": resposta_final})
    if memoria_activa:
        guardar_mensagem("assistant", resposta_final)