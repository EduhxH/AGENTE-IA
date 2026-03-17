🧠 Agente de IA Local com RAG












Um agente de IA com memória baseada em documentos, rodando 100% local. Sem nuvem. Sem atalhos. Só engenharia.

🧩 Sobre o Projeto

Este projeto é um laboratório prático para explorar LLMs locais e o padrão RAG (Retrieval-Augmented Generation).

A ideia foi simples e ambiciosa ao mesmo tempo:
criar um chat que não responde por adivinhação, mas sim consultando uma base de conhecimento construída a partir de documentos reais.

Tudo roda localmente, permitindo entender cada etapa:

📄 Ingestão de PDFs

🔢 Vetorização de texto

🧠 Busca semântica

💬 Geração de resposta com contexto

⚡ Como Funciona

O fluxo da aplicação é quase como uma pequena máquina pensante:

O utilizador faz uma pergunta

O sistema busca trechos relevantes no ChromaDB

Esses trechos viram o contexto do prompt

O modelo llama3.2 (via Ollama) gera a resposta

A resposta é exibida em tempo real (streaming)

💡 Traduzindo:
o modelo deixa de “inventar” e passa a consultar memória antes de falar

✨ Funcionalidades

🔍 Busca Semântica Inteligente
Utiliza similarity_search para encontrar os trechos mais relevantes.

🧠 Respostas com Contexto Real
O prompt é enriquecido com dados da base vetorial.

💬 Chat com Histórico
Mantém estado da conversa com st.session_state.

⚡ Streaming de Resposta
A resposta aparece aos poucos, como num modelo real (efeito ChatGPT).

🔒 Execução 100% Local
Nenhum dado sai da máquina.

🛠️ Stack Tecnológica

Streamlit → Interface de chat

LangChain → Orquestração do pipeline RAG

ChromaDB → Base de dados vetorial persistente

Ollama

llama3.2 → Modelo de linguagem

nomic-embed-text → Embeddings

📁 Estrutura do Projeto
RAG/
│
├── base/                  # PDFs utilizados
├── chroma_db/             # Base vetorial persistida
│
├── gabarito/
│   ├── app.py             # Interface + lógica do chat
│   ├── criar_db.py        # Script para gerar embeddings
│   └── .env
│
└── requirements.txt
⚙️ Como Executar
1️⃣ Instalar Ollama + modelos
ollama pull llama3.2
ollama pull nomic-embed-text
2️⃣ Instalar dependências
pip install -r requirements.txt
3️⃣ Criar a base vetorial (se necessário)
python criar_db.py
4️⃣ Executar o app
cd RAG/gabarito
streamlit run app.py
⚠️ Problemas Comuns
❌ Erro: banco não encontrado

Se aparecer:

Erro: Banco de dados não encontrado.

👉 Verifique se existe:

RAG/chroma_db

👉 Caso não exista, execute:

python criar_db.py
❌ Streamlit não encontra o app

Certifique-se de estar na pasta correta:

cd RAG/gabarito
🧪 Melhorias Futuras

📤 Upload de PDFs pela interface

🧠 Memória de longo prazo entre sessões

🎛️ Ajuste dinâmico de temperatura/modelo

🌐 Deploy local com Docker

📊 Visualização dos embeddings

🎯 Aprendizados

Este projeto explora na prática:

Como ligar dados → contexto → resposta

Diferença entre LLM puro vs RAG

Funcionamento interno de um sistema de IA real

<img width="787" height="383" alt="image" src="https://github.com/user-attachments/assets/ff6991ba-82fb-40fe-baf8-3c66d02ee3c6" /> 

(print do agente de IA)


<img width="1146" height="645" alt="image" src="https://github.com/user-attachments/assets/91887f90-40de-4637-beae-265e3e88d074" />

(Ollama)


<img width="1600" height="936" alt="image" src="https://github.com/user-attachments/assets/fa4e201b-3c12-4bc5-a963-cc5b7aa97192" />

(Streamlit)


<img width="960" height="960" alt="image" src="https://github.com/user-attachments/assets/3f316e02-7c36-4659-8afa-034a0ee6633b" />

(Python)


<img width="1400" height="733" alt="image" src="https://github.com/user-attachments/assets/3d4fd3aa-9239-4980-9622-28d0fa4efc93" />

(langchain)




