"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
rows = int(input())
matrix = []
columns = rows + 1
result = []
for i in range(rows):
    matrix.append(list(map(int,input().split())))
print(matrix)
for i in range(rows):
    for j in range(columns - 3):
        if matrix[i][j] == matrix[i][j+1] == matrix[i][j+2]==matrix[i][j+3]:
            result.append(matrix[i][j])
for i in range(rows-3):
    for j in range(columns):
        if matrix[i][j] == matrix[i+1][j] == matrix[i+2][j]== matrix[i+3][j]:
            result.append(matrix[i][j])
for i in range(rows-3):
    for j in range(columns-3):
        if matrix[i][j] == matrix[i+1][j+1] == matrix[i+2][j+2] == matrix[i+3][j+3]:
            result.append(matrix[i][j])
print(min(result))