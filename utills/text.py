from PyPDF2 import PdfReader
from langchain_text_splitters import CharacterTextSplitter #particionar um texto maior em chunks de texto


def process_files(files):

    text = ""

    for file in files:
        pdf = PdfReader(file)
        
        for page in pdf.pages:
            text += page.extract_text()
    
    return text


def creat_text_chunks(text):
    text_spliter = CharacterTextSplitter(
        separator='\n',
        chunk_size=1500,
        chunk_overlap=300,
        length_function = len
    )

    chunks = text_spliter.split_text(text)

    return chunks
