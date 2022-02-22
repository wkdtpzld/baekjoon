n, m = map(int, input().split())

arr = [[] for i in range(n)]
visited = [0] * n

for i in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(idx, x):
    if idx == 4:
        print(1)
        exit()

    for i in arr[x]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(idx+1,i)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(0,i)
    visited[i] = 0

print(0)