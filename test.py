from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader


def process_files():
    loader = PyPDFDirectoryLoader(
    "./pdfs"
    )
    text = loader.load()
    
    return text

def create_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 20,
    length_function = len,
    )
    
    chunks = text_splitter.split_documents(text)
    print(len(chunks)) # 11
    print(chunks[20])
    return chunks

text = process_files()
create_text_chunks(text)