import heapq
import sys

input = sys.stdin.readline

TC=int(input())

for i in range(TC):
    n = int(input())

    plus_h = []
    minus_h = []
    visited= [False] * n

    for j in range(n):
        a,b = map(str,input().split())

        if a == "I":
            heapq.heappush(plus_h,(-int(b),j))
            heapq.heappush(minus_h,(int(b),j))
            visited[j] = True

        if a == "D":
            if b == "1":
                while plus_h and not visited[plus_h[0][1]]:
                    heapq.heappop(plus_h)

                if plus_h:
                    visited[plus_h[0][1]] = False
                    heapq.heappop(plus_h)
            elif b == "-1":
                while minus_h and not visited[minus_h[0][1]]:
                    heapq.heappop(minus_h)

                if minus_h:
                    visited[minus_h[0][1]] = False
                    heapq.heappop(minus_h)


    while plus_h and not visited[plus_h[0][1]]:
        heapq.heappop(plus_h)
    while minus_h and not visited[minus_h[0][1]]:
        heapq.heappop(minus_h)

    if plus_h:
        print(-plus_h[0][0], minus_h[0][0])
    else:
        print("EMPTY")