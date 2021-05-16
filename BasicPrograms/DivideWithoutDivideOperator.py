"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def divide(x,y):
    quotient=0
    while x>=y:
        x=x-y
        quotient+=1
    #return x
    return quotient,x
x=6
y=2
print(divide(x,y))