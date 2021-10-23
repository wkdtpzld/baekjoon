import sys
sys.setrecursionlimit(100000)

n= int(input())
s=[list(map(int,input().split())) for i in range(n)]

dx,dy=[-1,1,0,0],[0,0,-1,1]

def dfs(x,y,h):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == 0 and s[nx][ny] > h:
                visit[nx][ny] = 1
                dfs(nx,ny,h)

result = 1

for h in range(max(map(max, s))):
    visit = [[0]*n for _ in range(n)]
    safe = 0
    for i in range(n):
        for j in range(n):
            if s[i][j] > h and visit[i][j] == 0:
                safe += 1
                visit[i][j] = 1
                dfs(i,j,h)
    result = max(safe,result)


print(result)