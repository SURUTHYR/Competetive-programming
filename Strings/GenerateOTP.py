"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
num = input("enter the number")
res = ""
for n in range(len(num)):
    if n%2 != 0:
        square = int(num[n])**2
        res += str(square)
print(res)

