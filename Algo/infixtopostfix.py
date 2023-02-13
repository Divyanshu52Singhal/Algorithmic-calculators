import streamlit as st

#INCOMPLETE
def infix_to_postfix(expression):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = []
    postfix_list = []
    token_list = expression.split()

    for token in token_list:
        st.write(token + "   " + str(*postfix_list))
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)

        elif token == '(':
            op_stack.append(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (len(op_stack) != 0 and
                   prec[op_stack[-1]] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.append(token)

    while len(op_stack) != 0:
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)



def main():
    st.title("Infix to Postfix Conversion")

    expression = st.text_input("Enter an infix expression:")

    if st.button("Convert"):
        result = infix_to_postfix(expression)
        st.write(f"The postfix expression is: {result}")

if __name__ == '__main__':
    main()