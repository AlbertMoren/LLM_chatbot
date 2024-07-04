import streamlit as st


def main():
    st.set_page_config(page_title="Pergunte para seus PDF",page_icon=':books:')

    with st.sidebar:

        st.subheader('arquivos')
        pdf_docs = st.file_uploader('carregar arquivos',accept_multiple_files=True)
        

if __name__ == '__main__':
    main()