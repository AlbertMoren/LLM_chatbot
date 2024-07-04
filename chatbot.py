from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def creat_vectorstore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(moodel_name = "WhereIsAI/UAE-Large-V1")
    vectorstore = FAISS.from_text(texts=chunks, embedding = embeddings)

    return vectorstore

def create_conversation(vectorsote):
    llm = HuggingFaceHub(repor_id = 'google/flan-t5-large', model_kwargs={
        "max+length":512,
        "temperature": 0.1
    })

    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever = vectorsote.as_retriever(),
        memory=memory 
        )
    
    return conversation_chain