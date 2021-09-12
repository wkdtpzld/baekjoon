n,m=map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
result = []

def DFS():
    if len(result) == m:
        print(' '.join(map(str,result)))
        return
    for i in nums:
        result.append(i)
        DFS()
        result.pop()

DFS()
#구 ㅅ~