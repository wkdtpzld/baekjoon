from collections import deque
import sys

dx=[0,-1,0,1]
dy=[-1,0,1,0]

def bfs(x,y):
    q= deque()
    q.append([x,y])
    visit[x][y]= 1
    cnt = 1
    while q:
        i,j=q.popleft()
        for K in range(4):
            nx = i + dx[K]
            ny = j + dy[K]
            if 0 <= nx < m and 0 <= ny < n and visit[nx][ny] == 0:
                if K == 0:
                    if 1 & room[i][j]: continue
                elif K == 1:
                    if 2 & room[i][j]: continue
                elif K == 2:
                    if 4 & room[i][j]: continue
                elif K == 3:
                    if 8 & room[i][j]: continue
                visit[nx][ny] = 1
                q.append([nx,ny])
                cnt += 1
    return cnt

n,m=map(int,sys.stdin.readline().split())
room=[]
for _ in range(m):
    room.append(list(map(int,sys.stdin.readline().split())))
visit=[[0]*n for _ in range(m)]

room_cnt=0
room_size=0
result3 = 0
for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            room_cnt += 1
            room_size = max(bfs(i,j),room_size)
for i in range(m):
    for j in range(n):
        num = 1
        while num < 9:
            if num & room[i][j]:
                visit = [[0]*n for k in range(m)]
                room[i][j] -= num
                result3 = max(result3,bfs(i,j))
                room[i][j] += num
            num *= 2
print(room_cnt)
print(room_size)
print(result3)