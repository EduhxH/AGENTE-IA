import json
import os
from datetime import datetime

MEMORY_PATH = os.getenv("MEMORY_PATH", "RAG/memory_db")
MEMORY_FILE = os.path.join(MEMORY_PATH, "historico.json")
MAX_MENSAGENS = 50 


def _garantir_pasta():
    os.makedirs(MEMORY_PATH, exist_ok=True)


def carregar_historico() -> list:
    _garantir_pasta()
    if not os.path.exists(MEMORY_FILE):
        return []
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return []


def guardar_mensagem(autor: str, texto: str):
    _garantir_pasta()
    historico = carregar_historico()
    historico.append({
        "autor": autor,
        "texto": texto,
        "timestamp": datetime.now().isoformat()
    })

    historico = historico[-MAX_MENSAGENS:]
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def limpar_historico():
    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)