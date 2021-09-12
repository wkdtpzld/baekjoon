tc=int(input())

for i in range(tc):
    dp = [0, 1, 1, 1, 2, 2]
    n = int(input())
    for i in range(6,n+1):
        dp.append(dp[i-3]+dp[i-4]+dp[i-5])
    print(dp[n])