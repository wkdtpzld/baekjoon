import sys
n=int(input())

s=list(map(int,sys.stdin.readline().split()))
dp=[s[0]]
for i in range(n-1):
    dp.append(max(dp[i]+s[i+1],s[i+1]))
print(max(dp))
