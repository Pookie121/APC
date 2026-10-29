A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[1,1,1],[1,1,1],[1,1,1]]

for i in range(3):
    for j in range(3):
        print(A[i][j] + B[i][j], end=" ")
    print()
