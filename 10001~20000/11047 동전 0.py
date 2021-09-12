import sys
n,k =map(int,sys.stdin.readline().split())
li=[int(sys.stdin.readline())  for i in range(n)]
result = 0

while k>0:
    for i in reversed(range(len(li))):
        if li[i] > k :
            li.pop()
        elif li[i] <= k and k -li[i] >= 0:
            result += (k//li[i])
            k -= (k//li[i])*li[i]

print(result)