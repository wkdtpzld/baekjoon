import sys

n,m=map(int,sys.stdin.readline().split())
s=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
DP=[[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + s[i-1][j-1]

for _ in range(m):
    i,j,x,y = map(int,sys.stdin.readline().split())
    print(DP[x][y]-DP[x][j-1]-DP[i-1][y]+DP[i-1][j-1])