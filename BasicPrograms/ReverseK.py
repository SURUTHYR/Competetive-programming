k=2
l=[5,8,4,9,3,2]
for i in range(0,len(l),2):
     l[i:i+ k].reverse()
     i=i+k
     print(l)