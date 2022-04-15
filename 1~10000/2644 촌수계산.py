import sys

n=int(input())
arr=[[] for i in range(n+1)]
visited=[0]*(n+1)

x,y=map(int,input().split())
k = int(input())
visited[x] = 1

for i in range(k):
    a,b = map(int,sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(start, arr, visited):
    for i in arr[start]:
        if visited[i] == 0:
            visited[i] = visited[start] + 1
            dfs(i, arr, visited)

dfs(x, arr , visited)
if visited[y] == 0:
    print(-1)
else:
    print(visited[y]-1)
