Local RAG with Python and Flask

This application is designed to handle queries using a language model and a vector database. It generates multiple versions of a user query to retrieve relevant documents and provides answers based on the retrieved context.
Prerequisites

    Python 3: Ensure you have Python 3.x installed.
    Ollama: This app requires Ollama to be installed and running locally. Follow the Ollama installation guide to set it up.

Setup

    Clone the repository:

$ git clone https://github.com/your-repo/local-rag.git
$ cd local-rag

    Create a virtual environment:

$ python -m venv venv
$ source venv/bin/activate

# For Windows user
# venv\Scripts\activate

    Install dependencies:

$ pip install -r requirements.txt

    Run Ollama: Ensure Ollama is installed and running locally. Refer to the Ollama documentation for setup instructions.

    Install llm model

$ ollama pull mistral

    Install text embedding model

$ ollama pull nomic-embed-text

    Run Ollama

$ ollama serve

Running the App

$ python app.py

Conclusion
This app leverages a language model and a vector database to provide enhanced query handling capabilities. Ensure Ollama is running locally and follow the setup instructions to get started.