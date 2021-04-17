"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def is_divisible(num):
    s=sum(list(map(int,str(num))))
    if num % s == 0:
        return True
    else:
        return False
rows = int(input("enter the no:of rows"))
matrix = []
for i in range(rows):
    matrix.append(list(map(int,input().split())))
column = len(matrix[0])
for i in range(rows-1):
    for j in range(column-1):
        if (is_divisible(matrix[i][j]) and is_divisible(matrix[i][j+1]) and is_divisible(matrix[i+1][j]) and is_divisible(matrix[i+1][j+1])):
            print(matrix[i][j],matrix[i][j+1])
            print(matrix[i+1][j],matrix[i+1][j+1])
