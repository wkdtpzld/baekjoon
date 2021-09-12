import sys
n = int(input())
nums = list(map(int,sys.stdin.readline().split()))
x = 0

for i in range(n-1 , 0 , -1):
    if nums[i] > nums[i -1]:
        x = i-1
        break
for j in range(n-1 , 0 , -1):
    if nums[x] < nums[j]:
        nums[x], nums[j] = nums[j] , nums[x]
        nums = nums[:x+1] + sorted(nums[x+1:])
        for i in nums:
            print(i,end=' ')
        exit()
print(-1)

