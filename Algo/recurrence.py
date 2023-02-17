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


def recurrence_relation(n, coeffs, initial_conditions):
    k = len(coeffs)
    if n < k:
        return initial_conditions[n]
    else:
        result = 0
        for i in range(k):
            result += coeffs[i] * recurrence_relation(n-k+i, coeffs, initial_conditions)
        return result

st.title('Recurrence Relation Calculator')

k = st.number_input('Enter the order of the recurrence relation (k):', min_value=1, step=1)

coeffs = []
for i in range(k):
    coeff = st.number_input('Enter the coefficient for a(n-{}):'.format(k-i), value=1.0, step=0.1)
    coeffs.append(coeff)

initial_conditions = []
for i in range(k):
    initial_condition = st.number_input('Enter the initial condition for a({}):'.format(i), value=0.0, step=0.1)
    initial_conditions.append(initial_condition)

n = st.number_input('Enter n:', min_value=0, step=1)

result = recurrence_relation(n, coeffs, initial_conditions)

st.write('a({}) = {}'.format(n, result))
