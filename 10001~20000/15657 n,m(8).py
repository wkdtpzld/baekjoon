import sys

n,m=map(int,input().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
result=[]

def dfs(a):
    if a == m:
        print(' '.join(map(str,result)))
        return
    for i in range(n):
        if a == 0 or result[a - 1] <= nums[i]:
            result.append(nums[i])
            dfs(a+1)
            result.pop()
dfs(0)