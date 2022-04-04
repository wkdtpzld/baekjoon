n,m = map(int,input().split())

s = list(map(int,input().split()))

ans = 0
for i in range(1,m-1):
    left = max(s[:i])
    right = max(s[i+1:])

    compare = min(left,right)
    if s[i] < compare:
        ans += compare - s[i]


print(ans)