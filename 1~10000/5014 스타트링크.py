from collections import deque

F,S,G,U,D = map(int,input().split())

visited=[0]*(F+1)

visited[S] = 1

queue = deque([])
queue.append(S)

while queue:
    x = queue.popleft()

    if 0 < x+U <= F:
        if visited[x]+1 < visited[x+U] or visited[x+U] == 0:
            visited[x+U] = visited[x]+1
            queue.append(x+U)

    if 0 < x-D <= F:
        if visited[x]+1 < visited[x-D] or visited[x-D] == 0:
            visited[x-D] = visited[x]+1
            queue.append(x-D)


if visited[G] == 0:
    print("use the stairs")
else:
    print(visited[G]-1)