import streamlit as st
from streamlit_chat import message
from utills  import chatbot
from utills import text

def main():
    st.set_page_config(page_title="Pergunte para seus PDFs", page_icon=':books:')
    st.header("LLM em PDF")

    directory = "./pdfs"

    if 'conversation' not in st.session_state:
        st.session_state.conversation = None

    all_files_text = text.process_files(directory)
    chunks = text.create_text_chunks(all_files_text)
    vectorstore = chatbot.create_vectorstore(chunks)
    st.session_state.conversation = chatbot.create_conversation(vectorstore)
    st.success("PDFs processados e banco de dados vetorial criado!")

    userquestion = st.chat_input("Faça uma pergunta:")

    if userquestion and st.session_state.conversation:
        response = st.session_state.conversation(userquestion)['chat_history']
        for i, text_message in enumerate(response):
            if i % 2 == 0:
                message(text_message.content, is_user=True, key=str(i) + '_user')
            else:
                message(text_message.content, is_user=False, key=str(i) + '_bot')

if __name__ == '__main__':
    main()