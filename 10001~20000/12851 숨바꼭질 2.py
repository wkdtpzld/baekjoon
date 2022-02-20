from collections import deque

n,m = map(int,input().split())
visited = [[-1,0] for i in range(100001)]

queue = deque([])

queue.append(n)
visited[n][0] = 0
visited[n][1] = 1
cnt = 0

while queue:

    x = queue.popleft()

    for i in [x-1,x+1,x*2]:
        if 0 <= i < 100001:
            if visited[i][0] == -1 or visited[i][0] > visited[x][0]+1:
                visited[i][0] = visited[x][0] + 1
                visited[i][1] = visited[x][1]
                queue.append(i)

            elif visited[i][0] == visited[x][0] + 1:
                visited[i][1] += visited[x][1]

print(visited[m][0])
print(visited[m][1])