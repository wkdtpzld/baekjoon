# from collections import deque
# import sys
#
# dx = [0,1]
# dy = [1,0]
#
# n=int(input())
#
# s=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
# visited=[[0]*n for _ in range(n)]
#
# queue=deque([])
# queue.append([0,0])
# visited[0][0] = 1
#
# while queue:
#     y = queue[0][1]
#     x = queue[0][0]
#
#     if s[x][y] == 0:
#         break
#
#     for i in range(2):
#         nx = (dx[i]*s[x][y]) + x
#         ny = (dy[i]*s[x][y]) + y
#
#         if nx < n and ny < n and visited[nx][ny] == 0:
#             queue.append([nx,ny])
#             visited[nx][ny] = visited[x][y] + 1
#             queue.popleft()
#
# print(visited[n-1][n-1]-1)

import sys

n = int(input())
s = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for y in range(n):
    for x in range(n):
        if s[y][x] == 0:
            break
        nx = x + s[y][x]
        ny = y + s[y][x]
        if 0 <= nx < n:
            dp[y][nx] += dp[y][x]
        if 0 <= ny < n:
            dp[ny][x] += dp[y][x]

print(dp[n-1][n-1])