from collections import deque
import sys

input = sys.stdin.readline

dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(X,Y):
    queue = deque([])
    queue.append([X,Y])
    temp = deque([])
    temp.append([X,Y])
    sum_value = s[X][Y]
    visited[X][Y] = 1

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    if L <= abs(s[nx][ny]-s[x][y]) <= R:
                        visited[nx][ny] = 1
                        sum_value += s[nx][ny]
                        queue.append([nx,ny])
                        temp.append([nx,ny])

    if len(temp) > 1:
        c = len(temp)
        mean = sum_value // c
        for i in range(c):
            xx,yy = temp[i]
            s[xx][yy] = mean
            q.append([xx,yy])

        return 0
    else:
        return 1

def check(x, y):
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:
                if L <= abs(s[nx][ny] - s[x][y]) <= R:
                    return False
    return True


n,L,R=map(int,input().split())
q = deque()
cnt =  0

s=[]
for i in range(n):
    s.append(list(map(int,input().split())))
    for j in range(n):
        q.append([i,j])
flag = False

while not flag:
    visited=[[0]*n for i in range(n)]
    flag = True
    size = len(q)

    for _ in range(size):
        x,y = q.popleft()
        if visited[x][y] == 1 or check(x,y):
            continue
        if not bfs(x,y):
            flag = False
    if not flag:
        cnt += 1


print(cnt)