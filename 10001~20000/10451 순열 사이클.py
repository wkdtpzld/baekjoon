import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

tc=int(input())
for i in range(tc):
    n=int(input())
    s=list(map(int,input().split()))
    visited=[0]*n
    cnt = 0

    def dfs(x,visit):

        visit.append(x)
        visited[x] = 1
        if s[x]-1 not in visit and visited[s[x]-1] == 0:
            dfs(s[x]-1,visit)


    for j in range(n):
        if visited[j] == 0:
            dfs(j,[])
            cnt += 1
    print(cnt)

