n = int(input())

s = list(map(int,input().split()))
s_2 = s[::-1]

dp=[1]*n
dp_2=[1]*n

for i in range(n):
    for j in range(i):
        if s[i] > s[j]:
            dp[i] = max(dp[i],dp[j]+1)
        if s_2[i] > s_2[j]:
            dp_2[i] = max(dp_2[i],dp_2[j]+1)


dp_2 = dp_2[::-1]

answer = [0 for i in range(n)]
for i in range(n):
    answer[i] = dp[i] + dp_2[i] - 1

print(max(answer))