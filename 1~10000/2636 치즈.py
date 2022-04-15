from collections import deque

n,m = map(int,input().split())

s= [list(map(int,input().split())) for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):

    queue = deque([])
    queue.append([x,y])
    visited=[[0]*m for i in range(n)]
    visited[x][y] = 1

    while queue:
        a,b = queue.popleft()

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and s[nx][ny] == 1:
                    visited[nx][ny] = visited[a][b] + 1
                    queue.append([nx,ny])

    for i in visited:
        print(i)

bfs(3,1)