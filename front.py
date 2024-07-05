import streamlit as st
from streamlit_chat import message
from utills.chatbot import create_conversation, create_vectorstore
from utills.text import process_files,creat_text_chunks


def main():
    st.set_page_config(page_title="Pergunte para seus PDF",page_icon=':books:')

    st.header("LLm em")
    userquestion = st.text_input("Faça uma pergunta para me")

    if('conversation' not in st.session_state):
        st.session_state.conversation = None
    
    if (userquestion):
        response = st.session_state.conversation(userquestion)['chat_hystory'] 

        for i,text_mensage in enumerate(response):
            
            if (i % 2 == 0):
                message(text_mensage.content, is_user=True, key=str(i) + '_user')
            else:
                message(text_mensage.content, is_user=False, key=str(i) + '_bot')

    with st.sidebar:
        st.subheader('arquivos')
        pdf_docs = st.file_uploader('carregar arquivos',accept_multiple_files=True)
        
        if st.button("Processar"):
            all_files_text = process_files(pdf_docs)

            chunks = creat_text_chunks(all_files_text)

            vectorstore = create_vectorstore(chunks)

            st.session_state.conversation = create_conversation(vectorstore)


if __name__ == '__main__':
    main()