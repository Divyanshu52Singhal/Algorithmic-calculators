import streamlit as st
import sympy as sp

st.title('Differentiation Calculator')

# Get the user-defined function
func_str = st.text_input('Enter a function to differentiate:', value='sin(x)')

# Parse the function
try:
    x = sp.Symbol('x')
    variables = {"sin": sp.sin, "cos": sp.cos, "tan": sp.tan, "cot": sp.cot, "sec": sp.sec, "csc": sp.csc}
    func = sp.sympify(func_str, locals=variables)
    # Display the parsed function with exponent in subscript
    st.subheader('Parsed function:')
    parsed_func_str = sp.latex(func).replace('**', '_')
    st.latex(f"{parsed_func_str}")
except:
    st.write("Error: Invalid function. Please enter a valid function in terms of 'x'.")

# Differentiate the function
deriv = sp.diff(func, x)

# Display the result
st.subheader('Derivative:')
st.latex(f"{sp.latex(deriv)}")
