import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline

n,m = map(int,input().split())
start = int(input())

dp=[INF]*(n+1)
heap = []
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

def dijkstra(start):

    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        a,now = heapq.heappop(heap)

        if dp[now] < a:
            continue

        for w, node in graph[now]:

            next_a = a + w

            if next_a < dp[node]:

                dp[node] = next_a

                heapq.heappush(heap,(next_a,node))

dijkstra(start)

for i in range(1,n+1):
    print("INF" if dp[i] == INF else dp[i])