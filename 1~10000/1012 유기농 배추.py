#
# def dfs(x,y):
#     dx,dy=[-1,1,0,0],[0,0,-1,1]
#     for i in range(4):
#         nx,ny=x+dx[i],y+dy[i]
#         if 0 <= nx < M and 0 <= ny < N:
#             if matrix[nx][ny] == 1:
#                 matrix[nx][ny] -= 1
#                 dfs(nx,ny)
import sys
from collections import deque

dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(x,y):
    q= deque()
    q.append((x,y))
    done[x][y] = 1
    while q:
        xx,yy=q.popleft()
        for _ in range(4):
            nx = xx+dx[_]
            ny = yy+dy[_]

            if (0<=nx<n) and (0<=ny<m) and done[nx][ny] == -1:
                if matrix[nx][ny] == 1:
                    q.append((nx,ny))
                    done[nx][ny] = 1
t = int(input())
for __ in range(t):
    cnt = 0
    n,m,k=map(int,input().split())
    matrix=[[0]*m for _ in range(n)]
    done = [[-1]*m for _ in range(n)]

    for _ in range(k):
        a,b=map(int,input().split())
        matrix[a][b] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and done[i][j] == -1:
                bfs(i,j)
                cnt +=1
    print(cnt)
