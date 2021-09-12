import sys
sys.setrecursionlimit(100000)
def dfs(i):
    visit[i]=1
    for k in range(1,N+1):
        if matrix[i][k] == 1 and visit[k] == 0:
            dfs(k)

N,M=map(int,sys.stdin.readline().split())

matrix=[[0]*(N+1) for i in range(N+1)]
visit=[0 for d in range(N+1)]
cnt=0

for i in range(M):
    a,b=map(int,sys.stdin.readline().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

for i in range(1,N+1):
    if visit[i] == 0:
        dfs(i)
        cnt += 1
print(cnt)
