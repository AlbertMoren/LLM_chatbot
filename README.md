# Chatbot Baseado em PDFs com Inteligência Artificial

Projeto de um chatbot de propósito específico, que fornece respostas extraídas de PDFs.

Este projeto utiliza um modelo de linguagem (LLM) e um modelo de embeddings do Hugging Face para responder perguntas baseadas em PDFs carregados pelo usuário. Os textos dos PDFs são processados e armazenados em um banco de dados vetorial para consultas eficientes. Assim, o chatbot responde às perguntas com base no conteúdo dos PDFs

## Modelos Utilizados

- **LLM**: `FLAN-T5 large `
- **Modelo de Embeddings**: `instructor-large`


### Como Executar

1. **Clone o repositório e navegue para o diretório do projeto.**
2. **Crie um ambiente virtual e ative-o.**
3. **Instale as dependências do `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
6. **Execute o aplicativo usando Streamlit.**
   ```bash
   streamlit run front.py   
7. **Abra o navegador na URL fornecida e interaja com a aplicação.**