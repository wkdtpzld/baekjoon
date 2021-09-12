n=int(input())
dp=[1,1,0,1,1]
for i in range(5,n+1):
    if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0:
        dp.append(1)
    else:
        dp.append(0)
if dp[n] == 0:
    print('CY')
else:
    print('SK')