"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def rotate_matrix(inmatrix):
    for i in range(len(inmatrix)):
        for j in range(i,len(inmatrix)):
            inmatrix[i][j] , inmatrix[j][i] = inmatrix[j][i] , inmatrix[i][j]


    n=len(inmatrix)
    for i in range(n//2):
        for j in range(n):
            inmatrix[j][i] , inmatrix[j][n-1-i] = inmatrix[j][n-1-i] , inmatrix[j][i]
        return inmatrix
inmatrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix(inmatrix))