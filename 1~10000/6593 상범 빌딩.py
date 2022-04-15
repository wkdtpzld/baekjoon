from collections import deque

while True:
    L, R, C = map(int,input().split())

    if (L + R + C) == 0:
        exit()

    building = []

    visited = [[[0]*C for _ in range(R)] for _ in range(L)]

    S = []
    E = []
    for _ in range(L):
        building.append([list(input()) for i in range(R)])
        input()

    for z in range(L):
        for x in range(R):
            for y in range(C):
                if building[z][x][y] == "S":
                    S =[x,y,z]
                    visited[z][x][y] = 1
                if building[z][x][y] == "E":
                    E =[x,y,z]

    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz = [0,0,0,0,-1,1]

    queue = deque([])
    queue.append(S)
    flag = False

    while queue:
        x,y,z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < R and 0 <= ny < C and 0 <= nz < L:
                if visited[nz][nx][ny] == 0:
                    if building[nz][nx][ny] == "." or building[nz][nx][ny] == 'E':
                        visited[nz][nx][ny] = visited[z][x][y] + 1
                        queue.append([nx,ny,nz])


    if visited[E[2]][E[0]][E[1]] == 0:
        print("Trapped!")
    else:
        print("Escaped in %d minute(s)." % (visited[E[2]][E[0]][E[1]]-1))