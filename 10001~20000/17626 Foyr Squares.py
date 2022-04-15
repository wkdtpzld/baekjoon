import math
n = int(input())

dp = [0]*(n+1)
dp[1] = 1

for i in range(2, n+1):
    if i == int(math.sqrt(i))**2:
        dp[i] = 1
    else:
        dp[i] = i

print(dp)

for i in range(2, n+1):
    for j in range(1,int(math.sqrt(i))+1):
        print(i,j,(math.sqrt(i)))
        print(dp)
        dp[i] = min(dp[i],dp[j*j]+dp[i-j*j])

print(dp)