import streamlit as st
from scipy.integrate import quad
import numpy as np

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
st.title('Integration Calculator')

# Get the user-defined function
func_str = st.text_input('Enter a function to integrate:', value='x**2')

# Define the integration limits
a = st.number_input('Enter the lower limit:', value=0)
b = st.number_input('Enter the upper limit:', value=1)

# Try to parse the function
try:
    variables = {"x": np.linspace(a, b, 1000), "np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan,
                 "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan}
    func = lambda x: eval(func_str, variables, {"__builtins__": None})
    #func = lambda x: eval(func_str, variables)
    #func = lambda x: eval(func_str, {"__builtins__": None}, {"np": np, "sin": np.sin, "cos": np.cos, "tan": np.tan, "arcsin": np.arcsin, "arccos": np.arccos, "arctan": np.arctan})
    # Calculate the integral
    step = 0.001
    result = 0
    for x in np.arange(a, b, step):
        result += func(x) * step
    # Display the result
    st.write(f"The result of integration is: {result[-1]:.2f}")
except:
    st.write("Error: Invalid function. Please enter a valid function in terms of 'x'.")
