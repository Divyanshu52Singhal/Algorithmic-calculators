import streamlit as st


def converter(string):
    size=len(string)
    operation=['(',')','*','/','^','+','-']
    variables=[]
    for i in range(size):
        if string[i].isdigit():
            continue
        if string[i] not in operation:
            if string[i] not in variables:
                variables.append(string[i])
            
        #print(variables)
    return variables


def changevalue(equation,variable,value):
    ev=''
    for i in equation:
        #print(i)
        if i in variable:
            pos=variable.index(i)
            ev+=str(value[pos])
        else:
            ev+=i
    st.write("ANSWER IS "+str(ev))

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
st.title("CREATE YOUR OWN CALCULATOR")

st.write("^ for power \n\n / for divide \n\n *for multiply \n\n +for addition\n\n -for subraction")

st.text_input(label="",placeholder="Enter the expression",
              key="expression")

input_of_web=st.session_state["expression"]
if input_of_web:
    s=input_of_web
    L=converter(s)
    value=[]
    for i in range(len(L)):
        st.text_input(label=L[i], placeholder="Enter the value",
                      key="value"+str(i))
        temp=st.session_state["value"+str(i)]
        s=s.replace(L[i],temp)
    s=s.replace("^","**")
    if temp:
        tri=eval(s)
        output="ANSWER IS "+ str(tri)
        st.title(output)