from langchain_community.document_loaders import PyPDFDirectoryLoader, PyPDFLoader
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_experimental.text_splitter import SemanticChunker  # type: ignore
from dotenv import load_dotenv
import warnings
import hashlib
import os
from datetime import datetime

warnings.filterwarnings("ignore", category=UserWarning, module="chromadb")
load_dotenv()

PASTA_BASE = os.getenv("PASTA_BASE", "RAG/base")
CHROMA_PATH = os.getenv("CHROMA_PATH", "RAG/chroma_db")
OLLAMA_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=OLLAMA_URL)


def carregar_documentos():
    if not os.path.exists(PASTA_BASE):
        print(f"Diretório não encontrado: {PASTA_BASE}")
        return []
    loader = PyPDFDirectoryLoader(PASTA_BASE, glob="**/*.pdf")
    docs = loader.load()
    print(f"Documentos carregados: {len(docs)} páginas")
    return docs


def carregar_pdf_bytes(nome_ficheiro: str, conteudo_bytes: bytes) -> list:
    """Carrega um PDF a partir de bytes (usado no upload via Streamlit)."""
    caminho_temp = os.path.join(PASTA_BASE, nome_ficheiro)
    os.makedirs(PASTA_BASE, exist_ok=True)
    with open(caminho_temp, "wb") as f:
        f.write(conteudo_bytes)
    loader = PyPDFLoader(caminho_temp)
    docs = loader.load()
    print(f"PDF '{nome_ficheiro}' carregado: {len(docs)} páginas")
    return docs


def dividir_texto(documentos: list) -> list:
    splitter = SemanticChunker(
        embeddings,
        breakpoint_threshold_type="percentile",
        breakpoint_threshold_amount=95
    )
    chunks = splitter.split_documents(documentos)

    for chunk in chunks:
        nome = os.path.basename(chunk.metadata.get("source", "desconhecido"))
        chunk.metadata["doc_name"] = nome
        chunk.metadata["indexed_at"] = datetime.now().isoformat()
        chunk.metadata["chunk_size"] = len(chunk.page_content)

    print(f"Chunks gerados: {len(chunks)}")
    return chunks


def gerar_id(chunk) -> str:
    conteudo = (
        chunk.page_content
        + str(chunk.metadata.get("source", ""))
        + str(chunk.metadata.get("page", ""))
    )
    return hashlib.md5(conteudo.encode()).hexdigest()


def gerar_vetores(chunks: list) -> dict:
    """Indexa chunks novos, ignora os já existentes. Retorna estatísticas."""
    print(f"A processar base de dados em: {CHROMA_PATH}")

    ids = [gerar_id(chunk) for chunk in chunks]
    banco = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    existentes = set(banco.get()["ids"])

    novos_chunks = [c for c, id_ in zip(chunks, ids) if id_ not in existentes]
    novos_ids = [id_ for id_ in ids if id_ not in existentes]

    if not novos_chunks:
        print("Nenhum documento novo encontrado. Base de dados já está actualizada.")
        return {"novos": 0, "total": len(existentes)}

    banco.add_documents(documents=novos_chunks, ids=novos_ids)
    print(f"Adicionados {len(novos_chunks)} chunks novos.")
    return {"novos": len(novos_chunks), "total": len(existentes) + len(novos_chunks)}


def executar():
    documentos = carregar_documentos()
    if documentos:
        chunks = dividir_texto(documentos)
        gerar_vetores(chunks)
    else:
        print("Operação cancelada: pasta de PDFs vazia.")


if __name__ == "__main__":
    executar()