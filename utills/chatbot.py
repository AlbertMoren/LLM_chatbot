from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFaceHub,Ollama
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,ChatPromptTemplate


def create_vectorstore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    
    return vectorstore

def create_conversation(vectorstore):
    # general_system_template = """
    # Você é um assistente virtual, que responde exclusivamente em português sobre os conteúdos dos PDFs armazenados.
    # Use o contexto fornecido para responder à pergunta de forma clara e concisa.
    # Se e pergunta for fora do contexto dos PDFs, responda que não pode responder fora do tópico.:

    # {context}

    # ---

    # Answer the question based on the above context: {question}
    # """
    # general_user_template = "Question:```{question}```"
    # messages = [
    #             SystemMessagePromptTemplate.from_template(general_system_template),
    #             HumanMessagePromptTemplate.from_template(general_user_template)
    # ]
    # qa_prompt = ChatPromptTemplate.from_messages( messages )

    llm = Ollama(model="llama3",temperature= 0.1)

    memory = ConversationBufferMemory(memory_key='chat_history' ,return_messages=True)
    conversation_chain =  ConversationalRetrievalChain.from_llm(
        llm,
        retriever=vectorstore.as_retriever(),
        memory=memory,
        combine_docs_chain_kwargs={'prompt': qa_prompt}
    )
    return conversation_chain 

