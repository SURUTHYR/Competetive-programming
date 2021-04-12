"""
@Author : 
Time complexity : O(nlogn)
Space complexity : O(1)
Question link :
"""
def quick_sort(list):
    n=len(list)
    recquick_sort(list,0,n-1)
def recquick_sort(list,first,last):
    if first<last:
        pos=partition(list,first,last)
        recquick_sort(list,first,pos-1)
        recquick_sort(list,pos+1,last)
def partition(list,first,last):
    pivot=list[first]
    i=first+1
    j=last
    while(i<j):
        while(i<= j and list[i]<=pivot):
            i=i+1
        while(j>=i and list[j]>=pivot):
            j=j-1
        if i<j:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
    temp=list[first]
    list[first]=list[j]
    list[j]=temp
    return j
list=[67,45,90,3,34]
quick_sort(list)
print(list)

