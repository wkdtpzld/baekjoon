from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y):
    global n, m, answer

    queue = deque([])
    queue.append([x, y])
    visited = [[0] * m for i in range(n)]
    visited[x][y] = 1
    cnt = 0

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < n and 0 <= ny < m:
                if s[nx][ny] == "L" and visited[nx][ny] == 0:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[a][b] + 1
                    if visited[nx][ny] > cnt:
                        cnt = visited[nx][ny]

    if answer < cnt:
        answer = cnt


n,m = map(int,input().split())

s = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0

for i in range(n):
    s.append(list(input()))

for i in range(n):
    for j in range(m):
        if s[i][j] == 'L':
            if j != 0 and j != m-1:
                if s[i][j-1] == "L" and s[i][j+1] == "L":
                    continue
            if i != 0 and i != n-1:
                if s[i-1][j] == "L" and s[i+1][j] == "L":
                    continue
            bfs(i,j)

print(answer-1)
