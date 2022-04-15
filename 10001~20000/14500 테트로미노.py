def dfs(x,y,idx,total):
    global ans
    if ans >= total + max_value * (3-idx):
        return
    if idx == 3:
        ans = max(ans,total)
        return
    else:
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visit[nx][ny] == 0:
                    if idx == 1:
                        visit[nx][ny] = 1
                        dfs(x,y,idx+1,total+s[nx][ny])
                        visit[nx][ny] = 0
                    visit[nx][ny] =1
                    dfs(nx, ny, idx + 1, total + s[nx][ny])
                    visit[nx][ny] = 0


n,m = map(int,input().split())

s = []
for i in range(n):
    s.append(list(map(int,input().split())))

visit = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
max_value = max(map(max,s))

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i,j,0,s[i][j])
        visit[i][j] = 0

print(ans)