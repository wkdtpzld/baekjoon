import sys
from collections import deque

n,m=map(int,input().split())
queue=deque([])
s=[]
for i in range(m):
    s.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if s[i][j] == 1:
            queue.append([i,j])

dx,dy=[-1,1,0,0],[0,0,-1,1]

while queue:
    x,y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if s[nx][ny] == 0:
                queue.append([nx,ny])
                s[nx][ny] = s[x][y] + 1

max_s = 0

for i in s:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        max_s = max(max_s,j)
print(max_s-1)
