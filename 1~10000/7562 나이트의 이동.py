from collections import deque

TC=int(input())
for i in range(TC):
    n= int(input())

    matrix=[[0]*n for _ in range(n)]

    a,b=map(int,input().split())
    result_a,result_b=map(int,input().split())

    matrix[a][b] = 1
    queue=deque([])
    queue.append([a,b])

    dx,dy=[2,1,-2,-1,-2,-1,2,1],[1,2,-1,-2,1,2,-1,-2]

    while queue:
        x,y=queue[0][0],queue[0][1]
        if x == result_a and y == result_b:
            print(matrix[x][y]-1)
            break

        queue.popleft()

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == 0:
                    queue.append([nx,ny])
                    matrix[nx][ny] = matrix[x][y] + 1
