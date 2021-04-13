from Stack import Stack


def check(s):
    st = Stack()
    dict = {'{': '}', '[': ']', '(': ')'}

    # Traverse the string
    for i in s:
        # check open
        if i == '{' or i == '[' or i == '(':
            # push into stack
            st.push(i)
        # close
        elif i == '}' or i == ']' or i == ')':
            # pop from stack
            if(st.is_empty()):
                return False

            temp = st.pop()
            # dict[pop] = i
            if dict[temp] == i:
                return False
    if(st.is_empty()):
        return True
    return False


str = "{[()]}("
print(check(str))
