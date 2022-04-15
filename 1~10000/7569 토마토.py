import sys
from collections import deque

m,n,h = map(int,input().split())

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,-1,1]

s=[]
for i in range(h):
    temp=[list(map(int,sys.stdin.readline().split())) for j in range(n)]
    s.append(temp)



queue=deque([])

for i in range(len(s)):
    for j in range(len(s[i])):
        for k in range(len(s[i][j])):
            if s[i][j][k] == 1:
                queue.append([i,j,k])



while queue:
    z,x,y=queue.popleft()

    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z

        if 0 <= nx < n and 0<= ny < m and 0 <= nz < h:
            if s[nz][nx][ny] == 0:
                queue.append([nz,nx,ny])
                s[nz][nx][ny] = s[z][x][y] + 1

last = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if s[i][j][k] == 0:
                print(-1)
                exit(0)
        last = max(last, max(s[i][j]))

print(last-1)