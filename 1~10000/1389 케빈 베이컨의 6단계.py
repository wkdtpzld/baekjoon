import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

s = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())

    s[a][b] = 1
    s[b][a] = 1

visited = [0]*(n+1)
result = [sys.maxsize]

for i in range(1,n+1):
    visited[i] = 1
    queue = deque([])
    queue.append(i)

    while queue:
        x = queue.popleft()

        for j in range(len(s[x])):
            if s[x][j] == 1 and visited[j] == 0:
                queue.append(j)
                visited[j] = visited[x] + 1

    result.append(sum(visited)-n)
    visited = [0]*(n+1)

print(result.index(min(result)))