"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def palindrome(sum):
    srev = str(sum)
    sumrev = srev[::-1]
    if sum == sumrev:
        return True
    print(len(sumrev))
n = int(input("enter the number"))
s = str(n)
reverse = s[::-1]
print(reverse)

if n == int(reverse):
    print("palindrome")
else:
    sum=int(n)+int(reverse)
    print(sum)
    palindrome(sum)
