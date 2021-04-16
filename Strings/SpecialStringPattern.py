"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
s = input("enter the string")
alnum = ""
res = ""
for char in s:
    if char.isalnum():
        alnum+=char
        print(alnum)
index = len(alnum)-1
for char in s:
    if char.isalnum():
        res+=alnum[index]
        index=index-1
    else:
        res+=char
print(res)