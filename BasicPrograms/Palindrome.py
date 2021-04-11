def check_palindrome(s):
    print(s)
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(str(d))
    count=0
    for i in d:
        if(d[i]%2!=0):
            count+=1
    if(count>1):
        print("It is not a palindrome")
    else:
        print("It is a palindrome")
check_palindrome("suruthy")
