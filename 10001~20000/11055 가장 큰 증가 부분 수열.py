n=int(input())
s = list(map(int,input().split()))
dp=[i for i in s]
for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] = max(dp[i],dp[j]+s[i])
print(max(dp))