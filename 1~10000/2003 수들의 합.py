n,m=map(int,input().split())
nums=list(map(int,input().split()))
sum_a=[0]*(n+1)
for i in range(1,n+1):
    sum_a[i] = sum_a[i-1] + nums[i-1]

answer=0

for i in range(n):
    for j in range(i+1,n+1):
        if sum_a[j] < m:
            pass
        elif sum_a[j] - sum_a[i] > m:
            break
        elif sum_a[j] - sum_a[i] == m:
            answer += 1
            break
print(answer)