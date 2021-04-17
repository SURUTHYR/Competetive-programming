"""
@Author : 
Time complexity :
Space complexity : 
Question link :https://codeofgeeks.com/great-sum/
"""
import itertools
l=list(map(int,input().split(",")))
s=int(input())
res=list(itertools.combinations(l,4))
c=0
for i in res:
    u=sum(i)
    if u == s:
       c+=1
    print(c)