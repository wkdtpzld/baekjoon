import sys

n=int(input())
s=list(map(int,sys.stdin.readline().split()))
s.sort()

x=int(input())

cnt = 0
int_sum = 0
start=0
end = n-1

while start < end:
    temp = s[start] + s[end]
    if temp == x:
        cnt += 1
        start += 1
    elif temp < x:
        start += 1
    else:
        end -= 1


print(cnt)
