n,m= map(int,input().split())

visited = [[0]*n for i in range(n)]

for i in range(m):
    a,b = map(int,input().split())
    visited[a][b] = 1

print(visited)