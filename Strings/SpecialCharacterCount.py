"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def mylist(list1,list2):
    res = []
    minlen = min(len(list1),len(list2))
    if (len(list1)==minlen):
        minlist = list1
        maxlist = list2
    else:
        minlist = list2
        maxlist = list1
        for index in range(0,minlen):
            res.append(list1[index])
            res.append(list2[index])
        res.extend(maxlist[minlen:])
        print(res)
s = input("enter the string")
evenlist = []
oddlist = []
scount = 0
for char in s:
    if (char.isdigit()):
        digit = int(char)
        if digit%2 == 0:
            evenlist.append(digit)
        else:
            oddlist.append(digit)

    else:
        scount+=1
if scount%2 == 0:
    mylist(evenlist,oddlist)
else:
    mylist(oddlist,evenlist)
