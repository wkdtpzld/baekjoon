N=int(input())
man=[list(map(int,input().split())) for _ in range(N)]
arr = [0]*N

for i in range(N):
    asd=[False for _ in range(N)]
    for grade in range(5):
        for j in range(N):
            if j != i and man[j][grade] == man[i][grade]:
                asd[j] = True
    arr[i] = len(list(filter(lambda x:x, asd)))
print(arr.index(max(arr))+1)