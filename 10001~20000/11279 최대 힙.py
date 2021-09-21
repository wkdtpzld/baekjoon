import heapq
import sys

s=[]

n=int(input())
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        try:
            print(-1 * heapq.heappop(s))
        except:
            print(0)
    else:
        heapq.heappush(s, (-a))