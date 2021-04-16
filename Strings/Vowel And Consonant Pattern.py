"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def consonant_vowel(word):

    for i in range(0,len(word)):
        if ((i%2==0 and word[i] not in vowel_list) or (i%2!=0 and word[i] in vowel_list)):
            pass
        else:
            return 0
    return 1

def vowel_consonant(word):
    for i in range(0,len(words)):
            if (i%2==0 and word[i]  in vowel_list ) or (i%2!=0 and word[i]  not in vowel_list):
                break
            else:
                return 0
    return 1


vowel_list = ['a','e','i','o','u']
s = input("enter the string")
words = s.split(",")

for word in words:
    word = word.lower()
    res1 = consonant_vowel(word)
    res2 = vowel_consonant(word)
    if(res1==1 or res2==1):
        print("valid")
    else:
        print("invalid")