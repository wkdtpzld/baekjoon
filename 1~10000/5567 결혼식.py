import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

group = [[0]*(n+1) for i in range(n+1)]

visited= [0]*(n+1)

m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    group[a][b] = 1
    group[b][a] = 1

cnt = 0
visited[1] = 1

queue = deque()
queue.append(1)

while queue:
    a = queue.popleft()

    for i in range(n+1):
        if group[a][i] == 1 and visited[i] == 0:
            visited[i] = visited[a] + 1

            queue.append(i)

for i in visited:
    if 1 < i < 4:
        cnt += 1

print(cnt)


# def dfs(start):
#     global cnt
#
#     for i in range(n+1):
#         if group[start][i] == 1 and visited[i] == 0:
#             cnt += 1
#             visited[i] = visited[start]+1
#             dfs(i)
#
# dfs(1)
