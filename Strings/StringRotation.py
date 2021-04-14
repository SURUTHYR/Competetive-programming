"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def rotate(s , value):
    square = 0
    while (value > 0):
        rem = value % 10
        square += rem ** 2
        value = value // 10
    sq = square
    print(sq)
    if sq%2==0:
        print(s[-1:]+s[:-1])
    else:
        r1 = 0
        r2 = 0
        r1 = str(s[1:]+s[:1])
        print(r1)
        r2 = str(r1[1:]+r1[:1])
        print(r2)



s = "rhdt"
value=246
#s="ghftd"
#value = 245
rotate(s , value)

