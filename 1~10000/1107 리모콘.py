n = int(input())

ans = abs(100 - n)

s_n = int(input())
if s_n:
    s = list(input().split())
else:
    s = list()

for num in range(1000001):
    for N in str(num):
        if N in s:
            break
    else:
        ans = min(ans,len(str(num))+abs(num-n))

print(ans)