from collections import deque

s=[]
n,m=map(int,input().split())
for i in range(n):
    s.append(list(map(int,input().split())))

nx=[-1,1,0,0]
ny=[0,0,-1,1]

max_result=0

def wall(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if s[i][j] == 0:
                s[i][j] = 1
                wall(cnt + 1)
                s[i][j] = 0
def bfs():
    global  max_result
    copy =[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = s[i][j]
    result = 0
    arr = deque([])
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                arr.append([i,j])
    while arr:
        a,b = arr[0][0] , arr[0][1]
        arr.popleft()
        for i in range(4):
            dx = a + nx[i]
            dy = b + ny[i]
            if 0 <= dx < n and 0 <= dy < m:
                if copy[dx][dy] == 0:
                    copy[dx][dy] = 2
                    arr.append([dx,dy])
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 0:
                result += 1
    max_result = max(result,max_result)

wall(0)
print(max_result)
