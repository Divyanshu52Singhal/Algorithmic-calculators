import streamlit as st


def focal_length(image_distance, object_distance):
    return 1 / ((1 / image_distance) + (1 / object_distance))



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
st.title("Focal Length Calculator")


st.text_input(label="Image Distance :",placeholder="Enter the value",
              key="id")
st.text_input(label="Object Distance :",placeholder="Enter the value",
              key="od")

image_distance = st.session_state["id"]
object_distance = st.session_state["od"]

if image_distance and object_distance:
    result = focal_length(float(image_distance), float(object_distance))
    st.write(f"<h3><b>Focal length of a lens is {result:.4f} units.</h3></b>",unsafe_allow_html=True)
