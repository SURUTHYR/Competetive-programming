"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def palindrome(num):
    p = int(num) + int(num[::-1])
    p = str(p)
    if p==str(p[::-1]):
        return p
    else:
        return palindrome(num)


num = input("enter the number")
print(palindrome(num))
