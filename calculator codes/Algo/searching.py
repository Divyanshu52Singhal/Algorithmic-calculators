import streamlit as st

page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-color:#E5B8F4;
    padding:none;
    margin:none;
    background-image: linear-gradient(0deg,#E5B8F4 ,#810CA8 );
    }
    </style>
    """
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title('String Search Calculator')

text = st.text_input('Enter some text:')
query = st.text_input('Enter a query string:')

if query in text:
    st.write(f'<h2><b>The query string is present in the text! at index = {text.find(query)+1}', unsafe_allow_html=True)
else:
    st.write('<h2><b>The query string is not present in the text.', unsafe_allow_html=True)
