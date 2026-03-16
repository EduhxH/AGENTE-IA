🧠 Meu Agente de IA (Chat RAG Local)
Criei esse projeto porque queria um assistente que realmente conhecesse meus documentos, mas sem que meus dados saíssem do meu computador. É um chat inteligente que usa RAG (Retrieval-Augmented Generation) pra responder dúvidas com base nos meus próprios arquivos, rodando 100% offline.


✨ O que ele faz?
Conversa com Contexto: Ele não chuta respostas; ele consulta a base de dados vetorial (ChromaDB) que eu criei.
Interface de Chat: Usei o Streamlit pra criar uma experiência parecida com o ChatGPT, com histórico de mensagens e tudo mais.
Privacidade Total: Como o "cérebro" é o Ollama (llama3.2), nada vai pra nuvem. Tudo fica na minha máquina.


🛠️ O que tem "debaixo do capô"
Streamlit: Pra interface web bonitona e fácil de usar.
Ollama (llama3.2 & nomic-embed-text): Os modelos que pensam e processam os textos.
LangChain + Chroma: A estrutura que conecta os PDFs à inteligência da IA.


🚀 Como rodar aí na sua máquina
Primeiro, você precisa ter o Ollama instalado e os modelos baixados (ollama pull llama3.2 e ollama pull nomic-embed-text).
Instale as bibliotecas:
bash
pip install streamlit langchain langchain-chroma langchain-ollama
Use o código com cuidado.

Verifique a base de dados:
Certifique-se de que a pasta RAG/chroma_db já existe com seus dados processados. O app vai te dar um erro amigável se não encontrar.
Dê o play:
bash
streamlit run app.py
Use o código com cuidado.


📝 Notas de quem fez
Este projeto foi um baita aprendizado sobre como unir uma interface web com modelos de linguagem locais. O próximo passo? Talvez colocar um botão pra fazer o upload de novos PDFs direto pela tela do chat! 🚀
