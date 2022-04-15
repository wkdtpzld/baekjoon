tc= int(input())
for i in range(tc):
    N,M,x,y = map(int,input().split())

    f = 1
    while (x <= N*M):
        if x%M == y%M:
            print(x)
            f = 0
            break
        x += N

    if f:
        print(-1)

