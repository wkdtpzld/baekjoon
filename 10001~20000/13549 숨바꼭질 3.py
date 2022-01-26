from collections import deque

n,m = map(int,input().split())

visited=[0]*100001

visited[n] = 1

queue = deque([])
queue.append(n)

while queue:

    x = queue.popleft()

    if 0 <= x*2 < 100001:
        if visited[x*2] < visited[x*2] or visited[x*2] == 0:
            visited[x*2] = visited[x]
            queue.append(x*2)

    if 0 <= x-1 < 100001:
        if visited[x-1] == 0 or visited[x-1] > visited[x]+1:
            visited[x-1] = visited[x]+1
            queue.append(x-1)
    if 0 <= x+1 < 100001:
        if visited[x+1] == 0 or visited[x+1] > visited[x]+1:
            visited[x+1] = visited[x]+1
            queue.append(x+1)

print(visited[m]-1)