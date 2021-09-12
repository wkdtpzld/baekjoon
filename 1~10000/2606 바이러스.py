# n=int(input())
# num=int(input())
# matrix=[[0]*(n+1) for _ in range(n+1)]
# for _ in range(num):
#     a,b=map(int,input().split())
#     matrix[a][b]=1
#     matrix[b][a]=1
#
#
# def dfs(start, visited):
#     visited += [start]
#     for c in range(len(matrix[start])):
#         if matrix[start][c] == 1 and c not in visited:
#             dfs(c,visited)
#     return visited
#
# print(len(dfs(1,[]))-1)

n=int(input())
num=int(input())
matrix=[[0]*(n+1) for _ in range(n+1)]
for _ in range(num):
    a,b=map(int,input().split())
    matrix[a][b],matrix[b][a] = 1,1

def dfs(start, visited):
    visited += [start]
    for c in range(len(matrix[start])):
        if matrix[start][c] == 1 and c not in visited:
            dfs(c,visited)
    return visited

print((dfs(1,[])))