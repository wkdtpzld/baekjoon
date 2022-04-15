n = int(input())

s = []

for i in range(n):
    x,y = map(int,input().split())
    s.append([x,y])


s.sort()

dp=[1]*n

for i in range(n):
    for j in range(i):
        if s[i][1] > s[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1

print(n-max(dp))