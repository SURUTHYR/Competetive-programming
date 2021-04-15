"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def pattern_matching(s):
    mylist = list(s)
    print(mylist)
    vowel_list = ['a','e','i','o','u']
    for i in range(len(mylist)):
        if (i%2==0 and i not in vowel_list) or (i%2!=0 and i in vowel_list):
                print("cv")

        else:
            if (i%2==0 and i  in vowel_list ) or (i%2!=0 and i not in vowel_list):
                print("vc")



s = "Badd"
pattern_matching(s)
