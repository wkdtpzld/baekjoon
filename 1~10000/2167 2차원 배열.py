n,m = map(int,input().split())
s = [list(map(int,input().split())) for i in range(n)]


DP=[[0 for __ in range(0,m+1)] for _ in range(0,n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1] + s[i-1][j-1]

for _ in range(int(input())):
    i , j , x , y = map(int,input().split())
    print(DP[x][y] - DP[x][j-1] - DP[i-1][y] + DP[i-1][j-1])
