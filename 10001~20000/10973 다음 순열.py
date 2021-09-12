n = int(input())
nums = list(map(int,input().split()))
x = -1

for i in range(n-1):
    if nums[i] > nums[i+1]:
        x = i

if x == -1:
    print(-1)
else:
    for i in range(x+1,n):
        if nums[x] > nums[i]:
            m = i

    nums[x], nums[m] = nums[m], nums[x]

    tmp = nums[x+1:]
    tmp.sort(reverse=True)
    nums = nums[:x+1] + tmp
    for j in nums:
        print(j,end=' ')
