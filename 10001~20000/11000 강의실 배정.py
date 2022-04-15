import heapq
import sys
input = sys.stdin.readline

n = int(input())

queue = []

for i in range(n):
    a,b = map(int,input().split())
    queue.append([a,b])

queue.sort()

room = []

heapq.heappush(room,queue[0][1])

for i in range(1,n):
    if queue[i][0] < room[0]:
        heapq.heappush(room,queue[i][1])

    else:
        heapq.heappop(room)
        heapq.heappush(room,queue[i][1])

print(len(room))