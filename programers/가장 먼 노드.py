import sys
import heapq

n = 6
vertex = [[3,6],[4,3],[3,2],[1,3],[1,2],[2,4],[5,2]]

def solution(n, vertex):

    INF = sys.maxsize

    dp=[INF]*(n+1)

    heap =[]

    edge = [[] for i in range(n+1)]
    for i in vertex:
        edge[i[0]].append((1,i[1]))
        edge[i[1]].append((1,i[0]))

    def dijkstra(start):

        dp[start] = 0

        heapq.heappush(heap,(0,start))

        while heap:

            a, now = heapq.heappop(heap)

            if dp[now] < a:
                continue

            for w, node in edge[now]:

                next_a = w + a

                if next_a < dp[node]:

                    dp[node] = next_a

                    heapq.heappush(heap,(next_a,node))

    def second(arr):

        two = one = -float('inf')

        for n in arr:
            if n > one:
                two = one
                one = n
            elif two < n < one:
                two = n

        return two

    dijkstra(1)
    search = second(dp)
    return dp.count(search)

print(solution(n,vertex))

