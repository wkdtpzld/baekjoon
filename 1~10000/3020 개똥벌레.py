import sys

input = sys.stdin.readline

n,h = map(int,input().split())

down=[0]*(h+1)
up=[0]*(h+1)
for i in range(n):
    if i % 2 == 0:
        up[int(input())] += 1
    else:
        down[h-int(input())+1] += 1

for i in range(h-1,0,-1):
    up[i] += up[i+1]

for i in range(1,h+1):
    down[i] += down[i-1]

min_cnt=n
range_cnt=0

for i in range(1,h+1):
    if min_cnt > (down[i]+up[i]):
        min_cnt = (down[i]+up[i])
        range_cnt = 1
    elif min_cnt == (down[i]+up[i]):
        range_cnt += 1

print(min_cnt,range_cnt)
print(up)
print(down)