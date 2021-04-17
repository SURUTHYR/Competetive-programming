"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""


def findfactsum(n):
    s = 1
    for j in range(2, n + 1):`
        if n % j == 0:
            s += j
    return s


res = []
l = list(map(int, input("enter the number").split(",")))
for i in l:
    val = findfactsum(i)
    if val in l:
        res.append(i)
if (len(res) == 0):
    print(-1)
else:
    print(sorted(res))



