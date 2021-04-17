"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
s = input("enter the string")
length = len(s)
unique = ''
for i in range(length):
    substring = s[i]
    for j in range(i+1,length):
        substring += s[j]
        sub_length = len(substring)
    if(sub_length>=3 and len(set(substring)) == sub_length):
        if len(unique)<sub_length:
            unique = substring
if len(unique) == 0:
    print(-1)
else:
    print(unique)
    print(len(unique))