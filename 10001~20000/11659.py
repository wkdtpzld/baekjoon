import sys

n,m=map(int,sys.stdin.readline().split())
nums=list(map(int,sys.stdin.readline().split()))
sum_num=[0]*(n+1)
for i in range(n+1):
    if i == 0:
        continue
    elif i == 1:
        sum_num[i] = nums[i-1]
    else:
        sum_num[i] = nums[i-1]+sum_num[i-1]
for j in range(m):
    a,b=map(int,sys.stdin.readline().split())
    print(sum_num[b]-sum_num[a-1])