"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
import math
instr = input("enter the string containing numbers")
temp = set()
outarr = []
for i in range(0 , len(instr)):
    for j in range(i , len(instr)):
        substring = int(instr[i:j+1])
        temp.add(substring)
temp = sorted(list(temp))
print("The substrings are",temp)
for num in temp:
    for value in range(1 , int(math.sqrt(num)+1)):
        if (value * value+1)== num:
            outarr.append(num)
            break


if outarr==[]:
    print(-1)
else:
    print(outarr)

