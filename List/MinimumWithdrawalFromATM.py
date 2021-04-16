"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
n=int(input())
x = []
for i in range(0,n):
    x.append(input())
x = list(map(int,x))
print(x)
k = int(input())
sum = 0
count = 0
while(1):
    if k==0:
        break
    if(len(x)==0):
        count=-1
        break
    h=x.pop()
    sum = sum+h
    count = count+1
    if sum>=k:
        break
print("Total withdrawal: ",end="")
print(count)