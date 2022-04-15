n=int(input())
li=[0]
for i in range(n):
    li.append(int(input()))

if n == 1:
    print(li[1])
else:
    dp = [0] * (n+1)
    dp[1] = li[1]
    dp[2] = li[1] + li[2]

    for i in range(3,n+1):
        dp[i] = max(dp[i-3]+li[i-1]+li[i],dp[i-2]+li[i])
    print(dp[n])