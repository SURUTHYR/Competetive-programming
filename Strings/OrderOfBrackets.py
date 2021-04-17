"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
s1=[]
op=['(','[','{']
cl=[')',']','}']
def validate(s):
    for i in range(len(s)):
        if s[i] in op:
            s1.append(s[i])
        elif s[i] in cl:
            res=cl.index(s[i])
            print(res)
            if(len(s1)>0) and (op[res]==s1[len(s1)-1]):
                s1.pop()
            else:
                return (i+1)
    if(len(s1)==0):
        return 0
    else:
        return len(s)+1
s=str(input())
print(validate(s))
