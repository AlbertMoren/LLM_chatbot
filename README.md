RAG local com Python e Streamlit

Esta aplicação foi projetado para lidar com consultas usando um modelo de linguagem(LLM) e um banco de dados vetorial(ChromaDB). Ele gera respostas com base no contexto fornecido em forma de consultas do usuário  usando como base os  documentos relevantes que serão previamente fornecido respostas  recuperado.

Pré-requisitos

    Python 3: Certifique-se de ter o Python 3 instalado.
    Ollama: Esta aplicação requer que o Ollama3 esteja instalado e funcionando localmente. Siga o guia de instalação do Ollama para configurá-lo.

Configuração inicial

    $ Clone o repositorio: https://github.com/AlbertMoren/LLM_chatbot
    $ cd local LLM_chatbot

Crie um ambiente virtual:

    $ python -m venv meu_ambiente_virtual
    $ source meu_ambiente_virtual/bin/activate

Para usuários de windows

    $ venv\Scripts\activate

Instalar dependências:

    $ pip install -r requirements.txt


Instalar modelo de llm 

    $ ollama run llama3
    $ /bye

Execultando a aplicação

    $ streamlit run app.py

Conclusão
Este aplicativo aproveita um modelo de linguagem e um banco de dados vetorial para fornecer recursos aprimorados de tratamento de consultas. Certifique-se de que o Ollama esteja sendo executado localmente e siga as instruções de configuração para começar.