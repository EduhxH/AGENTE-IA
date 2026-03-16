from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning, module="chromadb")
load_dotenv() 

PASTA_BASE = "RAG/base" 
CHROMA_PATH = "RAG/chroma_db"

def carregar_documentos():
    if not os.path.exists(PASTA_BASE):
        print(f"Diretório não encontrado: {PASTA_BASE}")
        return []
    
    loader = PyPDFDirectoryLoader(PASTA_BASE, glob="**/*.pdf")
    docs = loader.load()
    print(f"Documentos carregados: {len(docs)} páginas")
    return docs

def dividir_texto(documentos):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True
    )
    chunks = splitter.split_documents(documentos)
    print(f"Chunks gerados: {len(chunks)}")
    return chunks

def gerar_vetores(chunks):
    print(f"A processar base de dados em: {CHROMA_PATH}")
    
    embeddings = OllamaEmbeddings(model="nomic-embed-text")

    Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=CHROMA_PATH
    )
    print("Base de dados atualizada.")

def executar():
    documentos = carregar_documentos()
    
    if documentos:
        chunks = dividir_texto(documentos)
        gerar_vetores(chunks)
    else:
        print("Operação cancelada: pasta de PDFs vazia.")

if __name__ == "__main__":
    executar()

