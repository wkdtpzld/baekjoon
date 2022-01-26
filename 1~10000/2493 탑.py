n = int(input())

s = list(map(int,input().split()))

stack = []
dp = [0] * n

for i in range(n):
    t = s[i]
    while stack and s[stack[-1]] < t:
        stack.pop()

    if stack:
        dp[i] = stack[-1] + 1

    stack.append(i)

print(' '.join(map(str,dp)))