list = []
n = int(input("Enter the list size "))
for i in range(0, n):
    print("Enter number at index", i, )
    item = int(input())
    list.append(item)
print("User list is ",list)
swapcount=0
for i in range(len(list)):
    for j in range(i):
        if(list[i]>=list[j]):
            swapcount+=1
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
            print(list)
            print(swapcount)
