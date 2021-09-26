import sys
from collections import deque

n,m=map(int,sys.stdin.readline().split())
li=[[] for _ in range(n+1)]


for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    li[b].append(a)

def bfs(s):
    queue=deque()
    queue.append(s)
    visited = [0] * (n + 1)
    visited[s] = 1
    cnt = 1
    while queue:
        temp = queue.popleft()
        for i in li[temp]:
            if visited[i] == 0:
                visited[i] = 1
                cnt += 1
                queue.append(i)
    return cnt
result=[]
max_s=0

for i in range(1,n+1):
    temp = bfs(i)
    if temp == max_s:
        result.append(i)
    if max_s < temp:
        max_s = temp
        result = []
        result.append(i)

print(*result)


# pypy제출안하면 무조건막힘 망겜임 이거