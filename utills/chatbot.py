from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.llms import HuggingFaceHub
from langchain_community.vectorstores import FAISS
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


def create_vectorstore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name = "WhereIsAI/UAE-Large-V1")
    vectorstore = FAISS.from_text(texts=chunks, embedding = embeddings)

    return vectorstore

def create_conversation(vectorstore):
    llm = HuggingFaceHub(repor_id = 'google/flan-t5-large', model_kwargs={"max_length":512,"temperature": 0.1})

    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever = vectorstore.as_retriever(),
        memory=memory 
        )
    
    return conversation_chain