n=int(input())
s=[0]
for i in range(n):
    s.append(int(input()))

dp=[0]*(n+1)

if n == 1:
    print(s[1])
else:
    dp[1] = s[1]
    dp[2] = s[1]+s[2]
    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+s[i-1]+s[i],dp[i-2]+s[i],dp[i-1])
    print(dp)
