"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
s=input("enter the employee details")
pwd = ''
indv= s.split(",")
#ename=employee_details[0]
#eid = employee_details[1]
#print(employee_details)
#print(ename)
#print(eid)
for person in indv:
    temp=''
    details = person.split(":")
    name = details[0]
    idval = list(set(details[1]))
    idval = sorted(idval)[::-1]
    for dig in idval:
        if (int(dig)<=len(name)):
            temp = name[int(dig)-1]
            break
    if (len(temp)==0):
        temp = 'X'
    pwd+=temp
print(pwd)

