"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def selection_sort(list):
    for i in range(len(list)-1):
        k=i
        for j in range(i+1,len(list)):
            if(list[j]<list[k]):
                k=j
        if(k!=i):
            temp=list[i]
            list[i]=list[k]
            list[k]=temp

list=[7,45,8,3,9,1]
selection_sort(list)
print(list)