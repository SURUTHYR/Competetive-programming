"""
@Author :
Time complexity :
Space complexity :
Question link :
"""
s = input("enter the string")
even_list = []
odd_list = []
for char in s:
    if char.isdigit():
        digit = int(char)
        if (digit%2 == 0 and  digit not in even_list):
            even_list.append(digit)
        elif digit%2 !=0 and digit not in odd_list:
            odd_list.append(digit)
if len(even_list)>0:
    even_list.sort()
    print(even_list)
    odd_list.sort()
    print(odd_list)
    temp = (even_list[1:]+odd_list[:])[::-1]+[even_list[0]]
    print(*temp)
else:
    print(-1)

