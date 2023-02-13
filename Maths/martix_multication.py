import streamlit as st
import numpy as np
import pandas as pd

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
st.title("Matrix Multiplication")

st.text_input(label="Number of Rows Of Matrix A",placeholder="Enter the value",
              key="ra")
st.text_input(label="Number of Rows Of Matrix B",placeholder="Enter the value",
              key="rb")
ra = st.session_state["ra"]
rb = st.session_state["rb"]

if ra:
    A=[]
    for i in range(int(ra)):
        st.text_input(label=f"Enter Row {i+1} values OF A", placeholder="Enter the value",
                      key="valuea" + str(i))
        temp = st.session_state["valuea" + str(i)]
        temp =temp.split()
        temp = [int(i) for i in temp]
        A.append(temp)
if rb:
    B=[]
    for i in range(int(rb)):
        st.text_input(label=f"Enter Row {i+1} values OF B", placeholder="Enter the value",
                      key="valueb" + str(i))
        temp = st.session_state["valueb" + str(i)]
        temp =temp.split()
        temp = [int(i) for i in temp]
        B.append(temp)


if ra and rb:
    try:
        result = np.dot(A,B)
        df = pd.DataFrame(result,
                          columns=('C%d' % i for i in range(1,len(result[0])+1)))
        st.write(f"<b><h3> ANSWER IS : </h3><b>",unsafe_allow_html=True)
        st.dataframe(df)
    except ValueError:
        st.write(f"<b><h3> INCOMPLETE OR INCORRECT DIMENSION OF MATRICES",unsafe_allow_html=True)