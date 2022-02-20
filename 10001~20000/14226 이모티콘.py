from collections import deque

n = int(input())

visited = [[-1 for _ in range(n+1)] for _ in range(n+1)]
queue = deque([])

queue.append([1,0])
visited[1][0] = 0

while queue:

    x,y = queue.popleft()

    if x-1 >= 0 and visited[x-1][y] == -1:
        queue.append([x-1,y])
        visited[x-1][y] = visited[x][y] + 1

    if x+y <= n and visited[x+y][y] == -1:
        queue.append([x+y,y])
        visited[x+y][y] = visited[x][y] + 1

    if visited[x][x] == -1:
        visited[x][x] = visited[x][y] + 1
        queue.append([x,x])

ans = -1

for i in range(n+1):
    if visited[n][i] != -1:
        if ans == -1 or ans > visited[n][i]:
            ans = visited[n][i]

print(ans)