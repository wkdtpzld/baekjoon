import bisect

n = int(input())

s = list(map(int,input().split()))

dp = [s[0]]

for i in range(n):
    if s[i] > dp[-1]:
        dp.append(s[i])
    else:
        idx = bisect.bisect_left(dp,s[i])
        dp[idx] = s[i]

print(len(dp))