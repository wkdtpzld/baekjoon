n= int(input())
li = list(map(int,input().split()))
dp=[1]

for i in range(1,n):
    d = []
    for j in range(i):
        if li[i] > li[j] :
            d.append(dp[j]+1)
    if len(d) ==  0:
        dp.append(1)
    else:
        dp.append(max(d))
print(max(dp))