import streamlit as st
from utills import chatbot, text

def main():
    st.set_page_config(page_title="Pergunte para seus PDF",page_icon=':books:')

    with st.sidebar:
        st.subheader('arquivos')
        pdf_docs = st.file_uploader('carregar arquivos',accept_multiple_files=True)
        
        if st.button("Processar"):
            all_files_text = text.process_files(pdf_docs)

            chunks = text.creat_text_chunks(all_files_text)

            vectorstore = chatbot.create_vectorstore(chunks)

            conversation = chatbot.create_conversation(vectorstore)
            

if __name__ == '__main__':
    main()