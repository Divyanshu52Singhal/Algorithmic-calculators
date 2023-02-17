import streamlit as st
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
st.title("Linear Equation Solver")


# Function to print the matrix
def PrintMatrix(a):
    df = pd.DataFrame(a,
                      columns=('C%d' % i for i in range(1, len(a[0]) + 1)))
    st.write(f"<b><h3> Final Augmented Matrix is :  </h3><b>", unsafe_allow_html=True)
    st.dataframe(df)


# function to reduce matrix to reduced
# row echelon form.
def PerformOperation(a, n):
    flag = 0
    for i in range(n):
        if (a[i][i] == 0):

            c = 1
            while ((i + c) < n and a[i + c][i] == 0):
                c += 1
            if ((i + c) == n):
                flag = 1
                break

            j = i
            for k in range(1 + n):
                temp = a[j][k]
                a[j][k] = a[j + c][k]
                a[j + c][k] = temp

        for j in range(n):

            # Excluding all i == j
            if (i != j):
                # Converting Matrix to reduced row
                # echelon form(diagonal matrix)
                p = a[j][i] / a[i][i]

                k = 0
                for k in range(n + 1):
                    a[j][k] = a[j][k] - (a[i][k]) * p

    return flag


def PrintResult(a, n, flag):
    st.write("<h2><b>Result is : </b></h2>",unsafe_allow_html=True)

    if (flag == 2):
        st.write("<h2><b>Infinite Solutions Exists</b></h2>",unsafe_allow_html=True)
    elif (flag == 3):
        st.write("<h2><b> No Solution Exists</b></h2>",unsafe_allow_html=True)

    # Printing the solution by dividing constants by
    # their respective diagonal elements
    else:
        for i in range(n):
            st.write("X%d = %.3f"%(i+1,a[i][n] / a[i][i]))


# To check whether infinite solutions
# exists or no solution exists
def CheckConsistency(a, n, flag):
    # flag == 2 for infinite solution
    # flag == 3 for No solution
    flag = 3
    for i in range(n):
        sum = 0
        for j in range(n):
            sum = sum + a[i][j]
            if (sum == a[i][j]):
                flag = 2

    return flag


st.text_input(label="Order Of matrix",placeholder="Enter the value",
              key="ra")

n = st.session_state["ra"]

#a = [[0, 2, 1, 4], [1, 1, 2, 6], [2, 1, 1, 7]]
A=[]
if n:
    for i in range(int(n)):
        st.text_input(label=f"Enter Row {i+1} values OF A", placeholder="Enter the value",
                      key="valuea" + str(i))
        temp = st.session_state["valuea" + str(i)]
        temp =temp.split()
        temp = [int(i) for i in temp]
        A.append(temp)
flag = 0
if n and len(A)==int(n):
    try:
        flag = PerformOperation(A, int(n))
        if (flag == 1):
            flag = CheckConsistency(A, int(n), flag)
        PrintMatrix(A)
        PrintResult(A, int(n), flag)
    except IndexError:
        st.write(f"<b><h3>INCOMPLETE/ERROR IN INPUT</h3></b>", unsafe_allow_html=True)