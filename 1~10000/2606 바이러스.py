# n=int(input())
# num=int(input())
# matrix=[[0]*(n+1) for _ in range(n+1)]
# for _ in range(num):
#     a,b=map(int,input().split())
#     matrix[a][b],matrix[b][a] = 1,1
#
# def dfs(start, visited):
#     visited += [start]
#     for c in range(len(matrix[start])):
#         if matrix[start][c] == 1 and c not in visited:
#             dfs(c,visited)
#     return visited
#
# print((dfs(1,[])))

from collections import deque

n=int(input())
nums=int(input())

matrix=[[0]*(n+1) for _ in range(n+1)]

for i in range(nums):
    a,b = map(int,input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

queue = deque([])
queue.append(1)

visited=[0]*(n+1)

while queue:
    x = queue.popleft()

    visited[x] = 1

    for i in range(1,n+1):
        if matrix[x][i] == 1 and visited[i] == 0:
            queue.append(i)

print(visited.count(1)-1)

# def dfs(start,visited):
#     visited += [start]
#     for i in range(n+1):
#         if matrix[start][i] == 1 and i not in visited:
#             dfs(i,visited)
#     return visited
#
# print(len(dfs(1,[]))-1)