"""
@Author : 
Time complexity :
Space complexity : 
Question link :https://codeofgeeks.com/word-manipulation/
"""
s=input("enter the string")
uniquestring = sorted(set(s.upper()))
print(uniquestring)
res = []

for i in range(len(uniquestring)):
    newstring = ""
    for j in s:

        if uniquestring[i]==j.upper():
            newstring+=j
    res.append(newstring)
print(res)
output = ""
while bool(res)==True:
    if len(res)!=0:
        output+=res[0]
        res=res[1:]

    if len(res)!=0:
        output+=res[-1]
        res.pop()
print(output)



