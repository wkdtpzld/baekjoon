import sys
from collections import deque
sys.setrecursionlimit(10**5)

TC = int(input())

nx = [-1,1,0,0]
ny = [0,0,-1,1]

def bfs(a,b):
    global cnt
    cnt += 1

    board[a][b] = 0
    queue = deque([])

    queue.append([a,b])

    while queue:

        x,y = queue.popleft()

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]

            if 0 <= dx < m and 0 <= dy < n:
                if board[dx][dy] == 1:
                    board[dx][dy] = 0
                    queue.append([dx,dy])


for _ in range(TC):
    n,m,k = map(int,input().split())

    cnt = 0

    board = [[0]*(n) for i in range(m)]

    for _ in range(k):
        a,b = map(int,input().split())
        board[b][a] = 1


    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                bfs(i,j)

    print(cnt)
