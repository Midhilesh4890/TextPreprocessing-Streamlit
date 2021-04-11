import streamlit as st
import neattext.functions as nfx
import pandas as pd

#Text Downloader 
import base64
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = "clean_text_result_{}_.txt".format(timestr)
    st.markdown("### Download File ### ")
    href = f'<a href="data:file/txt:base64,{b64}" download="{new_filename}">click here!!</a>'
    st.markdown(href,unsafe_allow_html=True)

def main():
    st.title('Text Cleaner App')

    menu = ["TextCleaner","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == 'TextCleaner':
        st.subheader("Text Cleaning")
        text_file = st.file_uploader("Upload Text File",type=['txt'])
        normalize_case = st.sidebar.checkbox("Normalize Case")
        clean_stopwords = st.sidebar.checkbox('Stopwords')
        clean_punctuations = st.sidebar.checkbox('Punctuations')
        clean_emails = st.sidebar.checkbox('Emails')
        clean_special_char = st.sidebar.checkbox('Special Characters')
        clean_numbers = st.sidebar.checkbox('Numbers')
        clean_urls = st.sidebar.checkbox('Urls')
        clean_emojis = st.sidebar.checkbox('Emojis')

        if text_file is not None:
            file_details = {"Filename":text_file.name,"Filesize":text_file.size,"Filetype":text_file.type}
            st.write(file_details)

            #Decode Text
            raw_text = text_file.read().decode('utf-8')
            col1,col2 = st.beta_columns(2)

            with col1:
                with st.beta_expander("Orginal Text"):
                    st.write(raw_text)
            
            with col2:
                with st.beta_expander("Processed Text"):
                    if normalize_case:
                        raw_text = raw_text.lower()

                    if clean_stopwords:
                        raw_text = nfx.remove_stopwords(raw_text)

                    if clean_numbers:
                        raw_text = nfx.remove_numbers(raw_text)
                    
                    if clean_urls:
                        raw_text = nfx.remove_urls(raw_text)

                    if clean_punctuations:
                        raw_text = nfx.remove_punctuations(raw_text)

                    if clean_special_char:
                        raw_text = nfx.remove_special_characters(raw_text)

                    if clean_emails:
                        raw_text = nfx.remove_emails(raw_text)

                    if clean_emojis:
                        raw_text = nfx.remove_emojis(raw_text)
                    
                    st.write(raw_text)

                    text_downloader(raw_text)

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()