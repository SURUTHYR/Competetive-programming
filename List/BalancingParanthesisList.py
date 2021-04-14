"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def balancing_paranthesis(expr):
    newdict = {'{': '}', '[': ']', '(': ')'}
    mylist=[]
    for char in expr:
        if char=='(' or char == '{' or char == '[':
            mylist.append(char)


        elif char == ')' or char == '}' or char == ']':
            if len(mylist)==0:
                return False
            temp = mylist.pop()
            if dict[temp] == char:
                return True
    if len(mylist) == 0:
        return True
    else:
        return False



expr="({})"
print(balancing_paranthesis(expr))
if balancing_paranthesis(expr):
    print("expression is balanced")
else:
    print("expression is not balanced")