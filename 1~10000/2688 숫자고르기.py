def dfs(x,idx):
    visited[x] = 1

    for i in matrix[x]:
        if visited[i] == 0:
            dfs(i,idx)
        elif visited[i] == 1 and i == idx:
            result.append(i)

n = int(input())

s1 = [i+1 for i in range(n)]
s2 = [int(input()) for i in range(n)]

matrix = [[] for i in range(n)]

for i in range(n):
    matrix[s1[i]-1].append(s2[i]-1)

result = []

for i in range(n):
    visited = [0] * n
    dfs(i,i)

print(len(result))
for i in result:
    print(i+1)