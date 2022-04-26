import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    x = int(input())
    heapq.heappush(heap,x)

if n == 1:
    print(0)
else:
    result = 0
    while len(heap) > 1:
        x_1 = heapq.heappop(heap)
        x_2 = heapq.heappop(heap)

        result += x_1 + x_2

        heapq.heappush(heap,(x_1+x_2))
    print(result)