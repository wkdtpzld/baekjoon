from collections import deque

n,m,k = map(int,input().split())

matrix = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

visited= [0]*(n+1)



def dfs(x):
    visited[x] = 1
    print(x,end=" ")

    for i in range(1,n+1):
        if matrix[x][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(k)

def bfs(x):
    queue=deque([])
    queue.append(x)
    visited[x] = 0
    while queue:
        x = queue.popleft()
        print(x,end=" ")
        for i in range(1,n+1):
            if visited[i] == 1 and matrix[x][i] == 1:
                queue.append(i)
                visited[i] = 0
print()
bfs(k)
