import sys
import heapq

n,m,k,start = map(int,input().split())
INF = sys.maxsize
input = sys.stdin.readline

city = [[] for i in range(n+1)]
dp=[INF]*(n+1)

for i in range(m):
    v,c = map(int,input().split())

    city[v].append((1,c))

heap = []

def dijkstra(start):
    dp[start] = 0

    heapq.heappush(heap,(0,start))

    while heap:
        w,now = heapq.heappop(heap)

        if dp[now] < w:
            continue

        for w_node, node in city[now]:

            newx_w = w+ w_node

            if newx_w < dp[node]:
                dp[node] = newx_w

                heapq.heappush(heap,(newx_w,node))

dijkstra(start)

result= 0

for i in range(len(dp)):
    if dp[i] == k:
        print(i)
        result += 1

if result == 0:
    print(-1)


