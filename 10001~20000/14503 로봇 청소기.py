r,c=map(int,input().split())

robot=list(map(int,input().split()))

s=[list(map(int,input().split())) for i in range(r)]

cnt = 0

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def solution(x,y,n):
    global cnt

    if s[x][y] == 0:
        s[x][y] = 2
        cnt += 1

    for i in range(4):
        nn = (n+3) % 4
        nx = x + dx[nn]
        ny = y + dy[nn]

        if s[nx][ny] == 0:
            solution(nx,ny,nn)
            return

        n = nn

    nn = (n+2) % 4
    nx = x + dx[nn]
    ny = y + dy[nn]

    if s[nx][ny] == 1:
        return

    solution(nx,ny,n)


solution(robot[0],robot[1],robot[2])
print(cnt)