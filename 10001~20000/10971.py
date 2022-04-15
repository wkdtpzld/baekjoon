import sys

n=int(input())
s=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited=[False]*n
min_value=sys.maxsize

def dfs(start,cur,cost):
    global visited, s, min_value

    if start == cur and visited.count(False) == 0:
        min_value = min(min_value,cost)

    for i in range(n):
        if visited[i]==False and s[cur][i] != 0 :
            visited[i] = True
            dfs(start,i,cost+s[cur][i])
            visited[i] = False

dfs(0,0,0)
print(min_value)