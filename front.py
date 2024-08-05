import streamlit as st
from streamlit_chat import message
import chatbot
import text


def main():
    st.set_page_config(page_title="Pergunte para seus PDF", page_icon=':books:')
    st.header("LLm em")
    user_question = st.text_input("Faça uma pergunta para mim")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    if user_question:
        response = st.session_state.conversation(user_question)['chat_history']
        for i, text_message in enumerate(response):
            if i % 2 == 0:
                message(text_message.content, is_user=True, key=str(i) + '_user')
            else:
                message(text_message.content, is_user=False, key=str(i) + '_bot')

    with st.sidebar:
        st.subheader('Arquivos')
        pdf_docs = st.file_uploader('Carregar arquivos', accept_multiple_files=True)
        if st.button("Processar"):
            all_files_text = text.process_files(pdf_docs)
            chunks = text.create_text_chunks(all_files_text)
            vectorstore = chatbot.create_vectorstore(chunks)
            st.session_state.conversation = chatbot.create_conversation(vectorstore)

if __name__ == '__main__':
    main()