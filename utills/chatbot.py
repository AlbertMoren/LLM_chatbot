from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

raw_prompt = PromptTemplate.from_template(
    """
    <s>[INST] Você é um assistente técnico brasileiro especializado em buscar informações em documentos PDF. Se você não tiver uma resposta com base nas informações fornecidas, diga que não foi encontrada nenhuma informação.[/INST] </s>
    [INST] {input}
           Contexto: {context}
           Resposta:
    [/INST]
    """
)

def create_vectorstore(chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(chunks, embeddings)
    
    return vectorstore

def create_conversation(vectorstore):
    llm = HuggingFaceHub(repo_id='tiiuae/falcon-7b', huggingfacehub_api_token='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', model_kwargs={
    "max_length": 500,
    "temperature": 0.1
})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever = vectorstore.as_retriever(combine_docs_chain_kwargs={'prompt': raw_prompt}),
        memory=memory
    )
    return conversation_chain

