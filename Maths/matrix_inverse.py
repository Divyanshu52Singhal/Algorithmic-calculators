import streamlit as st
import pandas as pd

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if determinant==0:
        return "MATRIX DETERMINANT IS 0 THOSE ITS INVALID"
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    cofactors=list(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


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
st.title("Matrix Inverse")

st.text_input(label="Number of Rows Of Matrix A",placeholder="Enter the value",
              key="ra")

R = st.session_state["ra"]
  
if R:
    A=[]
    for i in range(int(R)):
        st.text_input(label=f"Enter Row {i+1} values OF A", placeholder="Enter the value",
                      key="valuea" + str(i))
        temp = st.session_state["valuea" + str(i)]
        temp =temp.split()
        temp = [int(i) for i in temp]
        A.append(temp)

if R:
    try:
        ans=getMatrixInverse(A)
        df = pd.DataFrame(ans,
                          columns=('C%d' % i for i in range(1, len(ans[0]) + 1)))
        st.write(f"<b><h3> ANSWER IS : </h3><b>", unsafe_allow_html=True)
        st.dataframe(df)

    except IndexError:
        st.write(f"<b><h3>INCOMPLETE/ERROR IN INPUT</h3></b>",unsafe_allow_html=True)
    except ValueError:
        st.write(f"<b><h3>INVERSE IMPOSSIBLE</h3></b>",unsafe_allow_html=True)