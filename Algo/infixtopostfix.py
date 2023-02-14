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

def infix_to_postfix(expression):
    # Initialize an empty stack and an empty output string
    stack = []
    output = ""

    # Define the operator precedence dictionary
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}

    # Split the input expression into tokens
    tokens = expression.split()

    # Create an empty table to store the output for each iteration
    table = [("Item", "Stack", "Output")]

    # Iterate through each token
    for token in tokens:
        # If the token is an operand, append it to the output string
        if token.isalnum():
            output += token + " "
        # If the token is an operator, pop higher precedence operators from the stack and append them to the output string
        elif token in precedence:
            while stack and precedence[token] <= precedence.get(stack[-1], 0):
                output += stack.pop() + " "
            stack.append(token)
        # If the token is a left parenthesis, push it onto the stack
        elif token == "(":
            stack.append(token)
        # If the token is a right parenthesis, pop operators from the stack and append them to the output string until a left parenthesis is found
        elif token == ")":
            while stack and stack[-1] != "(":
                output += stack.pop() + " "
            stack.pop()

        # Append the current iteration's item, stack, and expression to the table
        table.append((token, ", ".join(stack), output))

    # Pop any remaining operators from the stack and append them to the output string
    while stack:
        output += stack.pop() + " "

    # Append the final postfix expression to the table
    table.append(("", "Final stack: " + ", ".join(stack), "Postfix: " + output))

    # Return the final postfix expression and the output table
    return output, table


# Define the Streamlit app
def app():
    st.title("Infix to Postfix Calculator")

    # Get the input infix expression from the user
    expression = st.text_input("Enter an infix expression:", "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3")

    # Convert the infix expression to postfix and get the output table
    postfix_expr, table = infix_to_postfix(expression)

    # Display the output table in a tabular format
    #st.table(table)
    if table:
        co1 , co2 , co3 = st.columns(3)
        with co1:
            for x in table:
                st.write(f"<b>{x[0]}",unsafe_allow_html=True)
        with co2:
            for x in table:
                st.write(f"<b>{x[1]}",unsafe_allow_html=True)
                if x[1] == "Stack":
                    st.write("")
        with co3:
            for x in table:
                st.write(f"<b>{x[2]}",unsafe_allow_html=True)

        # Display the final postfix expression
        st.write("<b><h3>Postfix expression:", postfix_expr,unsafe_allow_html=True)


app()
