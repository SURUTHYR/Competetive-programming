"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
s = input("enter the string")
n = len(s)
flag = 0
for index in range(n//2,0,-1):
    prefix = s[:index]
    suffix = s[n-index:]
    if prefix == suffix:
        flag = 1
        break
if flag==1:
    print(len(prefix))
else:
    print(-1)
