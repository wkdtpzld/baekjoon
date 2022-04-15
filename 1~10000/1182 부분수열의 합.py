import sys

n,m=map(int,input().split())
s=list(map(int,sys.stdin.readline().split()))

cnt = 0

def dfs(a,b):
    global cnt
    if a >= n:
       return
    b += s[a]
    if b == m:
        cnt += 1
    dfs(a+1, b - s[a])
    dfs(a+1, b)

dfs(0,0)
print(cnt)