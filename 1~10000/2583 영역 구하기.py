import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m,k = map(int,input().split())

s = [[0]*m for i in range(n)]

visited=[[0]*m for i in range(n)]

for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            s[i][j] = 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

def dfs(x,y):

    global cnt

    s[y][x] = 1
    visited[y][x] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n:
            if visited[ny][nx] == 0 and s[ny][nx] == 0:
                cnt += 1
                dfs(nx,ny)

    return cnt

result = []

for i in range(n):
    for j in range(m):
        if s[i][j] == 0 and visited[i][j] == 0:
            cnt = 0
            result.append(dfs(j,i))

print(len(result))

for i in sorted(result):
    print(i+1,end=" ")