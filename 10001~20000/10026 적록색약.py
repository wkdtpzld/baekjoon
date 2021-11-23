import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

n = int(input())

RGB = [list(input()) for i in range(n)]

visited = [[0]*(n) for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y,s):

    if RGB[x][y] == s:
        visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if RGB[nx][ny] == s and visited[nx][ny] == 0:
                dfs(nx,ny,s)

cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j,RGB[i][j])
            cnt += 1
print(cnt,end=" ")

for i in range(n):
    for j in range(n):
        if RGB[i][j] == "G":
            RGB[i][j] = "R"

visited = [[0]*(n) for i in range(n)]
cnt = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j,RGB[i][j])
            cnt += 1

print(cnt)