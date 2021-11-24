n = int(input())

s=[1,1,1,1,1,1,1,1,1,1]
dp=[1]
for j in range(n-1):
    for i in range(1,10):
        dp.append(sum(s[:i+1]))
    s = dp
    dp=[1]

print(sum(s)%10007)