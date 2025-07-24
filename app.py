import streamlit as st
import pandas as pd
import re

st.set_page_config(layout="wide")

df0 = pd.read_csv('data.csv')
df1 = df0[['volume_title', 'book_title', 'chapter_number', 'verse_number', 'text']]
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

with st.sidebar:
    st.title('LDS Standard Works Parallel App')
    st.write('This app was created for students of the LDS Standard Works and is especially userful for finding connections across the texts.')
    st.write('The ***Read*** tab allows the user to read up to three different chapters side-by-side.')
    st.write('The ***Search*** tab allows the user to search for occurences of specified text in up to three different places.')
    st.subheader('Acknowledgements')
    st.write("The scripture database used by this app was drawn from [Andrew Heiss'](https://github.com/andrewheiss/) [scriptuRs](https://github.com/andrewheiss/scriptuRs) package.")
    st.write('This app was made as part of the coursework for RELA 275 at Brigham Young University.')
    st.write('For feedback or suggestions, please feel free to [contact me on GitHub](https://github.com/jl240).')

tab1, tab2 = st.tabs(['Read', 'Search'])

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

with tab2:
    volumes = ['Old Testament', 'New Testament', 'Book of Mormon', 'Doctrine and Covenants', 'Pearl of Great Price']

    col1, col2, col3 = st.columns(3)
    
    with col1:
        subcol1, subcol2, subcol3 = st.columns(3)

        with subcol1:
            volume = st.selectbox('Volume', volumes, key='2.1.1')
            df20 = df1[df1['volume_title']==volume]
            books = df20['book_title'].unique().tolist()
            books.insert(0, 'All books')
        
        with subcol2:
            book = st.selectbox('Book', books, key='2.3.1')

        with subcol3:
            search_for = st.text_input("Exact text to search for:")

        if search_for:
            if book == 'All books':
                matches = df1[
                    (df1['volume_title'] == volume) &
                    (df1['text'].str.contains(search_for, case=False, na=False))
                ]
            else:
                matches = df1[
                    (df1['volume_title'] == volume) &
                    (df1['book_title'] == book) &
                    (df1['text'].str.contains(search_for, case=False, na=False))
                ]

            total_occurrences = sum(
                len(re.findall(re.escape(search_for), text, flags=re.IGNORECASE))
                for text in matches['text']
            )

            st.write(f"Found {total_occurrences} occurrence(s) of '{search_for}' in {len(matches)} verse(s).")
            st.markdown(
                """
                <style>
                hr {
                    margin-top: 0px;
                    margin-bottom: 1rem;
                    border: none;
                    border-top: 1px solid #ccc;
                }
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
                <hr>
                """,
                unsafe_allow_html=True
            )

            # Prepare list of highlighted verses as HTML strings
            highlighted_texts = []
            pattern = re.compile(re.escape(search_for), re.IGNORECASE)

            for _, row in matches.iterrows():
                highlighted = pattern.sub(
                    lambda m: f"<span style='background-color: rgba(30, 144, 255, 0.3)'>{m.group(0)}</span>",
                    row['text']
                )
                # Format each verse line with reference + highlighted text
                verse_line = f"<strong>{row['book_title']} {row['chapter_number']}:{row['verse_number']}</strong> – {highlighted}"
                highlighted_texts.append(verse_line)

            # Join all verses with spacing and wrap in scroll-box div
            all_text = "<br><br>".join(highlighted_texts)
            st.markdown(f'<div class="scroll-box">{all_text}</div>', unsafe_allow_html=True)

    with col2:
        subcol1, subcol2, subcol3 = st.columns(3)

        with subcol1:
            volume = st.selectbox('Volume', volumes, key='2.1.2')
            df20 = df1[df1['volume_title']==volume]
            books = df20['book_title'].unique().tolist()
            books.insert(0, 'All books')
        with subcol2:
            book = st.selectbox('Book', books, key='2.3.2')

        with subcol3:
            search_for = st.text_input("Exact text to search for:", key='2.2.2')

        if search_for:
            if book == 'All books':
                matches = df1[
                    (df1['volume_title'] == volume) &
                    (df1['text'].str.contains(search_for, case=False, na=False))
                ]
            else:
                matches = df1[
                    (df1['volume_title'] == volume) &
                    (df1['book_title'] == book) &
                    (df1['text'].str.contains(search_for, case=False, na=False))
                ]

            total_occurrences = sum(
                len(re.findall(re.escape(search_for), text, flags=re.IGNORECASE))
                for text in matches['text']
            )

            st.write(f"Found {total_occurrences} occurrence(s) of '{search_for}' in {len(matches)} verse(s).")
            st.markdown(
                """
                <style>
                hr {
                    margin-top: 0px;
                    margin-bottom: 1rem;
                    border: none;
                    border-top: 1px solid #ccc;
                }
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
                <hr>
                """,
                unsafe_allow_html=True
            )

            # Prepare list of highlighted verses as HTML strings
            highlighted_texts = []
            pattern = re.compile(re.escape(search_for), re.IGNORECASE)

            for _, row in matches.iterrows():
                highlighted = pattern.sub(
                    lambda m: f"<span style='background-color: rgba(30, 144, 255, 0.3)'>{m.group(0)}</span>",
                    row['text']
                )
                # Format each verse line with reference + highlighted text
                verse_line = f"<strong>{row['book_title']} {row['chapter_number']}:{row['verse_number']}</strong> – {highlighted}"
                highlighted_texts.append(verse_line)

            # Join all verses with spacing and wrap in scroll-box div
            all_text = "<br><br>".join(highlighted_texts)
            st.markdown(f'<div class="scroll-box">{all_text}</div>', unsafe_allow_html=True)

    with col3:
        subcol1, subcol2, subcol3 = st.columns(3)

        with subcol1:
            volume = st.selectbox('Volume', volumes, key='2.1.3')
            df20 = df1[df1['volume_title']==volume]
            books = df20['book_title'].unique().tolist()
            books.insert(0, 'All books')
        
        with subcol2:
            book = st.selectbox('Book', books, key='2.3.3')

        with subcol3:
            search_for = st.text_input("Exact text to search for:", key='2.2.3')

        if search_for:
            if book == 'All books':
                matches = df1[
                    (df1['volume_title'] == volume) &
                    (df1['text'].str.contains(search_for, case=False, na=False))
                ]
            else:
                matches = df1[
                    (df1['volume_title'] == volume) &
                    (df1['book_title'] == book) &
                    (df1['text'].str.contains(search_for, case=False, na=False))
                ]

            total_occurrences = sum(
                len(re.findall(re.escape(search_for), text, flags=re.IGNORECASE))
                for text in matches['text']
            )

            st.write(f"Found {total_occurrences} occurrence(s) of '{search_for}' in {len(matches)} verse(s).")
            st.markdown(
                """
                <style>
                hr {
                    margin-top: 0px;
                    margin-bottom: 1rem;
                    border: none;
                    border-top: 1px solid #ccc;
                }
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
                <hr>
                """,
                unsafe_allow_html=True
            )

            # Prepare list of highlighted verses as HTML strings
            highlighted_texts = []
            pattern = re.compile(re.escape(search_for), re.IGNORECASE)

            for _, row in matches.iterrows():
                highlighted = pattern.sub(
                    lambda m: f"<span style='background-color: rgba(30, 144, 255, 0.3)'>{m.group(0)}</span>",
                    row['text']
                )
                # Format each verse line with reference + highlighted text
                verse_line = f"<strong>{row['book_title']} {row['chapter_number']}:{row['verse_number']}</strong> – {highlighted}"
                highlighted_texts.append(verse_line)

            # Join all verses with spacing and wrap in scroll-box div
            all_text = "<br><br>".join(highlighted_texts)
            st.markdown(f'<div class="scroll-box">{all_text}</div>', unsafe_allow_html=True)



