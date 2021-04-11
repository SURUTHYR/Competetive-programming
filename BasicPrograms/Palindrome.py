def check_palindrome(s):
    print(s)
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(d)
    v=d.values()
    print(v)
    for i in v:
        if (v==1):
            print("True")
        else:
            print("False")


check_palindrome("aba")
