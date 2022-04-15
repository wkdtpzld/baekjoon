import sys
import heapq

n = int(input())
m = int(input())

input = sys.stdin.readline
INF = sys.maxsize
heap = []

dp=[INF]*(n+1)
city=[[] for i in range(n+1)]

for i in range(m):
    u,m,v = map(int,input().split())
    city[u].append((v,m))

def dijkstra(start):

    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        w_now,now = heapq.heappop(heap)

        if dp[now] < w_now:
            continue

        for wei,node in city[now]:

            next_w = w_now + wei

            if dp[node] > next_w:
                dp[node] = next_w
                heapq.heappush(heap,(next_w,node))

start,end=map(int,input().split())

dijkstra(start)

print(dp[end])