import copy
import sys

n,m = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

Detector=[
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[0,3]],
    [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
    [[0,1,2,3]]
]

s = []
cctv = []

answer = sys.maxsize

for i in range(n):
    data = list(map(int,input().split()))
    s.append(data)
    for j in range(m):
        if data[j] in [1,2,3,4,5]:
            cctv.append([data[j],i,j])

def fill(arr,nn,x,y):
    for i in nn:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 > nx or 0 > ny or n <= nx or m <= ny:
                break
            if arr[nx][ny] == 6:
                break
            elif arr[nx][ny] == 0:
                arr[nx][ny] = 7

def dfs(idx,arr):
    global answer

    if idx == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        answer = min(answer,count)

        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[idx]
    for i in Detector[cctv_num]:
        fill(temp,i,x,y)
        dfs(idx+1,temp)
        temp = copy.deepcopy(arr)

dfs(0,s)
print(answer)