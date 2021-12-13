from itertools import combinations

n = int(input())

nums = [0,1,2,3,4,5,6,7,8,9]

s = []
for i in range(1,11):
    temp = list(combinations(nums,i))
    for j in temp:
        a = sorted(j)
        num = 0
        for x in range(i):
            num += (10**x)*a[x]
        s.append(num)

s.sort()

try:
    print(s[n])
except IndexError:
    print(-1)
