from math import floor
import sys

n,m=map(int,sys.stdin.readline().split())
z = floor(100 * m/n)

start , end = 0 , 1000000000
if z >= 99:
    print(-1)
else:
    while start <= end:
        mid = (start + end) // 2
        nn , nm = n + mid, m + mid
        if floor(100 * nm/nn) > z:
            end = mid - 1
        else:
            start = mid + 1
    print(end + 1)
