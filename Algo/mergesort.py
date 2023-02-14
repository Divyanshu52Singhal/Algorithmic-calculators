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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        st.write("Iteration:", *L,*R)
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        st.write("Current:", *arr)
    return arr


def main():
    st.title("Merge Sort Visualization")
    st.text_input("Enter a list of numbers separated by commas:",key="e")
    arr=st.session_state["e"]
    if arr:
        arr=arr.split(',')
        arr = [int(i) for i in arr]
        st.write("Original list:", *arr)
        sorted_arr = merge_sort(arr)
        st.write("Sorted list:", *sorted_arr)


main()
