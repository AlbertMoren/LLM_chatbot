from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate




def create_vectorstore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings)
    
    return vectorstore

def create_conversation(vectorstore):
    llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b', huggingfacehub_api_token='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', model_kwargs={
    "max_length": 512,
    "temperature": 0.5,
    "return_full_text" : False
})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever = vectorstore.as_retriever(search_type="similarity_score_threshold",
                                    search_kwargs={'score_threshold': 0.8},
                ),
        memory=memory,
    )
    return conversation_chain

