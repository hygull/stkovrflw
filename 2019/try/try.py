def transpose(A):
    output = [[''] * len(A[0]) for i in range(len(A))]
    
    for i in range(len(A[0])):
        for j in range(len(A)):
            output[j][i] = A[i][j]

    return output

a = [[1,2,3],[4,5,6],[7,8,9]]
a = transpose(a)
# [[1,4,7],[2,5,8],[3,6,9]]
print(a) 
