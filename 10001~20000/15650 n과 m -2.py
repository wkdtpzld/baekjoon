n,m=map(int,input().split())
result=[]
def dfs(s):
    if len(result) == m:
        print(' '.join(map(str,result)))
    for i in range(s,n+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()
dfs(1)