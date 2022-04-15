n,m=map(int,input().split())

s=[list(input()) for i in range(n)]

nx=[-1,1,0,0]
ny=[0,0,-1,1]

visited=[[0,0]]
s[0][0] = 1


while visited:
    a,b=visited[0][0],visited[0][1]

    del visited[0]

    for i in range(4):
        xx=a+nx[i]
        yy=b+ny[i]
        if n > xx >= 0 and m > yy >= 0:
            if s[xx][yy] == '1':
                visited.append([xx,yy])
                s[xx][yy] = s[a][b] + 1
print(s[n-1][m-1])