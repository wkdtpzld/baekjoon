import sys
import heapq

# INF = sys.maxsize
n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

# island = [[] for i in range(n)]
# dp = [INF]*n
# for i in costs:
#     island[i[0]].append((i[2],i[1]))
#     island[i[1]].append((i[2],i[0]))
#
# heap = []
#
# def dijkstra(start):
#
#     dp[start] = 0
#
#     heapq.heappush(heap,(0,start))
#
#     while heap:
#
#         w,node = heapq.heappop(heap)
#
#         if dp[node] > w:
#             continue
#
#         for ww, node_next in island[node]:
#
#             next_w = w + ww
#
#             if next_w < dp[node_next]:
#
#                 dp[node_next] = next_w
#
#                 heapq.heappush(heap,(next_w,node_next))
#
# answer = []
# result = 0
#
# for i in range(n):
#     dijkstra(i)
#     answer.append(dp)
#     dp = [INF] * n
#
# for i in range(n):
#     print(answer[i])

answer = 0
costs.sort(key= lambda x: x[2])
connect = set([costs[0][0]])

while len(connect) != n:
    for cost in costs:
        if cost[0] in connect and cost[1] in connect:
            continue
        if cost[0] in connect or cost[1] in connect:
            connect.update([cost[0],cost[1]])

            answer += cost[2]
            break

print(answer)