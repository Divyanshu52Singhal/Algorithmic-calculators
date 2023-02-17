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
st.title("COULOMB'S LAW")

st.text_input(label="Charge on Q1",placeholder="Enter the value",
              key="q1")
st.text_input(label="Charge on Q2",placeholder="Enter the value",
              key="q2")
st.text_input(label="Distance Between both charges in meters",placeholder="Enter the value",
              key="r")
q1 = st.session_state["q1"]
q2 = st.session_state["q2"]
r  = st.session_state["r"]
if q1 and q2 and r:
    Force  =   (9*float(q1)*float(q2)/float(r)*float(r))*(10**(-3))
    st.write(f"<b><h3> Force is : {abs(Force):.4f} N </h3><b>",unsafe_allow_html=True)

