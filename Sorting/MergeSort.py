def merge_sort(list):
    if len(list)>1:
        mid=len(list)//2
        llist=list[:mid]
        rlist=list[mid:]
        merge_sort(llist)
        merge_sort(rlist)
        i=0
        j=0
        k=0
        while i < len(llist) and j < len(rlist):
            if llist[i]<rlist[j]:
                list[k]=llist[i]
                i=i+1
            else:
                list[k]=rlist[j]
                j=j+1
            k=k+1
        while i < len(llist):
            list[k]=llist[i]
            i=i+1
            k=k+1
        while j < len(rlist):
            list[k]=rlist[j]
            j=j+1
            k=k+1
list=[90,56,87,34]
merge_sort(list)
print(list)