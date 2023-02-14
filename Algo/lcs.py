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

def lcs(x, y):
    m = len(x)
    n = len(y)
    # Create a matrix to store the lengths of LCS of substrings of x and y
    lcs_lengths = [[0] * (n + 1) for _ in range(m + 1)]
    # Fill the matrix in bottom-up manner
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                lcs_lengths[i][j] = 0
            elif x[i-1] == y[j-1]:
                lcs_lengths[i][j] = lcs_lengths[i-1][j-1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i-1][j], lcs_lengths[i][j-1])
    # Traverse the matrix to find the LCS
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:
            lcs = x[i-1] + lcs
            i -= 1
            j -= 1
        elif lcs_lengths[i-1][j] > lcs_lengths[i][j-1]:
            i -= 1
        else:
            j -= 1
    return lcs

st.title("Longest Common Subsequence Finder")
x = st.text_input("Enter the first string:")
y = st.text_input("Enter the second string:")
if st.button("Find LCS"):
    lcs = lcs(x, y)
    st.write(f"<b><h3>The longest common subsequence of : \n\n<b><h3> '{x}' \n\n <b><h3> AND <b>\n\n <b><h3>'{y}' \n\n<b><h3> IS \n\n<b><h3>'{lcs}'", unsafe_allow_html=True)
