"""
@Author : 
Time complexity :
Space complexity : 
Question link :
"""
def diagonal(m):
    sum = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if(i==j):
                sum+=m[i][j]
    print(sum)
                #if i+j==2:
                    #print(m[i][j])

m=[[1,2,3] ,[4,5,6],[7,8,9]]
diagonal(m)
