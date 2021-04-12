"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
from Stack import Stack
def eval_postfix(exp):
    for token in exp:
        if token.isdigit():
            st.push(int(token))
        elif token=='+':
            operand2=st.pop()
            operand1=st.pop()
            result=operand1+operand2
            st.push(result)
        elif token=='-':
            operand2 = st.pop()
            operand1 = st.pop()
            result = operand1 - operand2
            st.push(result)
        elif token=='*':
            operand2 = st.pop()
            operand1 = st.pop()
            result = operand1 * operand2
            st.push(result)
        elif token=='/':
            operand2 = st.pop()
            operand1 = st.pop()
            result = operand1 / operand2
            st.push(result)
        else:
            print("mismatch")
    return st.pop()

st=Stack()
exp="35+6-"
print(eval_postfix(exp))
