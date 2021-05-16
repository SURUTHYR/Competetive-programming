"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def multiply(num1,num2):
    product=0
    for i in range(1,num2+1):
        product+=num1
    return product
num1=5
num2=2
print(multiply(num1,num2))