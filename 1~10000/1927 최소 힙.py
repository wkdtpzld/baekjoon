import heapq
import sys

n= int(sys.stdin.readline())
heap = []
for i in range(n):
    a = int(sys.stdin.readline())
    if a == 0 and len(heap) == 0:
        print(0)
    elif a == 0 and len(heap) != 0:
        print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,a)

