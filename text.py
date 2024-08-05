from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter

def process_files(files):
    text = ""
    for file in files:
        pdf = PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text()
    return text

def create_text_chunks(text):
    print(text)
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return text_splitter.create_documents(chunks)
