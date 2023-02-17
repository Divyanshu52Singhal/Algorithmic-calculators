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

st.title("Calculator with Previous Calculation")

prev_result = 0
calculation = []
results = []

def calculate(expression):
    try:
        result = eval(expression)
        results.append(result)
        calculation.append(expression + ' = ' + str(result))
        return result
    except:
        return 'Error'

def reset_calculation():
    global calculation, results
    calculation = []
    results = []

def view_calculation():
    if len(calculation) == 0:
        return 'No previous calculation'
    else:
        return '\n\n'.join(calculation)

def display_calculations(result):
    st.write('Result: ', result)
    st.write('Previous Calculations: ')
    st.write(view_calculation())

i=0
while True:
    expression = st.text_input('Enter expression:',key=i)
    i+=1
    if expression:
        result = calculate(expression)
        display_calculations(result)
    else:
        if st.button('Sum OF ALL Previous Result',key="k"+str(i)):
            st.write('SUM: ', sum(results))
        elif st.button("RESET",key="j"+str(i)):
            reset_calculation()
            st.write('Calculations have been reset!')
            st._rerun()
        else:
            break