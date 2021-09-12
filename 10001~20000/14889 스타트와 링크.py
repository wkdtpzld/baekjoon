n=int(input())
matrix=[]
for i in range(4):
    matrix.append(list(map(int,input().split())))

for i in range(n-1):
    for j in range(n):
        if matrix[i][j] != 0:
            print(matrix[i][j])