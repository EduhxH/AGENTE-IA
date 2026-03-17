🧠 Meu Agente de IA (Chat RAG Local)

Criei este projeto como um laboratório pessoal. O meu principal objetivo foi mergulhar de cabeça no mundo dos LLMs (Large Language Models) e entender como o RAG (Retrieval-Augmented Generation) funciona na prática.
Mais do que apenas um chat, este projeto foi a minha forma de aprender a conectar inteligência artificial com dados reais, mantendo tudo rodando localmente para entender cada etapa do processo — desde a vetorização de documentos até a interface final.


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


📝 Notas:

Este projeto foi um baita aprendizado sobre como unir uma interface web com modelos de linguagem locais. O próximo passo? Talvez colocar um botão pra fazer o upload de novos PDFs direto pela tela do chat! 🚀

👍LEIA CASO TENHA PROBLEMAS:

É comum que as vezes dê erro no streamlit, no qual o programa não executa pois não consegue achar o ficheiro app.py ou a pasta da db, para isso deve se seguir os seguintes passos:

1- Acede à pasta do script:
Navega até ao diretório onde o ficheiro principal está localizado:
cd RAG/gabarito

2- Inicia o Streamlit:
Executa o comando abaixo para abrir a aplicação no teu navegador:
streamlit run app.py

Nota: Certifica-te de que o terminal está na pasta correta (onde o app.py reside) para que as dependências e o banco de dados sejam carregados corretamente.

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




