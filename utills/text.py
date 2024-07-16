from langchain_text_splitters import  RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader


def process_files():
    loader = PyPDFDirectoryLoader(
    "./pdfs"
    )
    text = loader.load()
    
    return text

def create_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 300,
    separators=["\n\n", "\n", " ", ""]
    )
    chunks = text_splitter.split_documents(text)
    return chunks