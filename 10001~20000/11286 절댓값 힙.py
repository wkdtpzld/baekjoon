import sys
import heapq

heap=[]
input = sys.stdin.readline

n=int(input())

for i in range(n):
    s = int(input())
    if s != 0:
        heapq.heappush(heap,(abs(s),s))
    else:
        try:
            print(heapq.heappop(heap)[1])
        except IndexError:
            print(0)