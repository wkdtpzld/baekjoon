n,m=map(int,input().split())
nums=list(map(int,input().split()))
result=[]

def dfs():
    if len(result) == m:
        print(''.join(map(str,result)))
    for i in nums:
        if i not in result:
            result.append(i)
            dfs()
            result.pop()

dfs()