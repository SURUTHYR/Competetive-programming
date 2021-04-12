"""
@Author : 
Time complexity : O(n^2)
Space complexity : O(1)
Question link :
"""


def insertion_sort(list):
    for i in range(1, len(list)):
        k = i - 1
        current_element = list[i]
        while k >= 0 and list[k] > current_element:
            list[k + 1] = list[k]
            k = k - 1
        list[k + 1] = current_element


list = [56, 34, 24, 21, 12]
insertion_sort(list)
print(list)
