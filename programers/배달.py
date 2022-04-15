import sys
import heapq
from bisect import bisect_left, bisect_right

INF = sys.maxsize

N = 5
road =[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

dp=[INF]*(N+1)

heap=[]

city=[[] for i in range(N+1)]

for i in road:
    city[i[0]].append((i[2],i[1]))
    city[i[1]].append((i[2],i[0]))

def dijkstra(start):

    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        a, now = heapq.heappop(heap)

        if dp[now] < a:
            continue

        for w, node in city[now]:

            next_a = a + w

            if next_a < dp[node]:

                dp[node] = next_a

                heapq.heappush(heap,(next_a,node))

dijkstra(1)

dp.sort()

def cnt(a,left,right):
    r = bisect_right(a,right)
    l = bisect_left(a,left)
    return r-l


print(cnt(dp,0,K))