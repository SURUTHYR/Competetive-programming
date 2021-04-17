"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
l=[x for x in input("enter the number").split(",")]
num1 = 0
first_index = l.index('5')
last_index = l.index('8')
mylist = l[:first_index]+l[last_index+1:]
for num in mylist:
    num1+=int(num)
print(num1)
num2= "".join(l[first_index:last_index+1])
print(num2)
sum=num1+int(num2)
print(sum)