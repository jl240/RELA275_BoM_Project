import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df0 = pd.read_csv('data.csv')
df1 = df0[['volume_title', 'book_title', 'chapter_number', 'verse_number', 'text']]

tab1, tab2 = st.tabs(['Read', 'TBD'])

with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
        subcol1, subcol2, subcol3 = st.columns(3)

        with subcol1:
            volumes = df1['volume_title'].unique()
            volume = st.selectbox('Volume', volumes, key='1.1')
            df10 = df1[df1['volume_title']==volume]

        with subcol2:
            books = df10['book_title'].unique()
            book = st.selectbox('Book', books, key='1.2')
            df11 = df10[df10['book_title']==book]

        with subcol3:
            chapters = df11['chapter_number'].unique()
            chapter = st.selectbox('Chapter', chapters, key='1.3')
            df12 = df11[df11['chapter_number']==chapter]

        df13 = df12[['verse_number', 'text']]

        text = [f'{row['verse_number']}  {row['text']}' for _, row in df13.iterrows()]

        scrollable_box_style = """
            <style>
            .scroll-box {
                max-height: 800px;
                overflow-y: auto;
                padding: 10px;
                border-radius: 5px;
                background-color: #0E1117;
                white-space: pre-wrap;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            """
        
        st.markdown(scrollable_box_style, unsafe_allow_html=True)

        text_content = "<br><br>".join(text)
        st.markdown(f'<div class="scroll-box">{text_content}</div>', unsafe_allow_html=True)

        
    with col2:
        subcol1, subcol2, subcol3 = st.columns(3)

        with subcol1:
            volumes = df1['volume_title'].unique()
            volume = st.selectbox('Volume', volumes, key='2.1')
            df10 = df1[df1['volume_title']==volume]

        with subcol2:
            books = df10['book_title'].unique()
            book = st.selectbox('Book', books, key='2.2')
            df11 = df10[df10['book_title']==book]

        with subcol3:
            chapters = df11['chapter_number'].unique()
            chapter = st.selectbox('Chapter', chapters, key='2.3')
            df12 = df11[df11['chapter_number']==chapter]

        df13 = df12[['verse_number', 'text']]

        text = [f'{row['verse_number']}  {row['text']}' for index, row in df13.iterrows()]

        scrollable_box_style = """
            <style>
            .scroll-box {
                max-height: 800px;
                overflow-y: auto;
                padding: 10px;
                border-radius: 5px;
                background-color: #0E1117;
                white-space: pre-wrap;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            """
        
        st.markdown(scrollable_box_style, unsafe_allow_html=True)

        text_content = "<br><br>".join(text)
        st.markdown(f'<div class="scroll-box">{text_content}</div>', unsafe_allow_html=True)

        
    with col3:
        subcol1, subcol2, subcol3 = st.columns(3)

        with subcol1:
            volumes = df1['volume_title'].unique()
            volume = st.selectbox('Volume', volumes, key='3.1')
            df10 = df1[df1['volume_title']==volume]

        with subcol2:
            books = df10['book_title'].unique()
            book = st.selectbox('Book', books, key='3.2')
            df11 = df10[df10['book_title']==book]

        with subcol3:
            chapters = df11['chapter_number'].unique()
            chapter = st.selectbox('Chapter', chapters, key='3.3')
            df12 = df11[df11['chapter_number']==chapter]

        df13 = df12[['verse_number', 'text']]

        text = [f'{row['verse_number']}  {row['text']}' for index, row in df13.iterrows()]

        scrollable_box_style = """
            <style>
            .scroll-box {
                max-height: 800px;
                overflow-y: auto;
                padding: 10px;
                border-radius: 5px;
                background-color: #0E1117;
                white-space: pre-wrap;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            """
        
        st.markdown(scrollable_box_style, unsafe_allow_html=True)

        text_content = "<br><br>".join(text)
        st.markdown(f'<div class="scroll-box">{text_content}</div>', unsafe_allow_html=True)
