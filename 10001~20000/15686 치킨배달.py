from itertools import combinations
import sys

INF = sys.maxsize

n,m = map(int,input().split())

s = [list(map(int,input().split())) for i in range(n)]

cnt = 0

h = {}
c = []
for i in range(n):
    for j in range(n):
        if s[i][j] == 1:
            h[i,j] = INF
        elif s[i][j] == 2:
            c.append([i,j])

a = list(combinations(c,m))

result = INF

for i in a:
    answer = 0
    for j in h:
        h[j] = INF

    for y in i:
        for x in h:
            h[x] = min(h[x],abs(x[0]-y[0])+abs(x[1]-y[1]))

        result = min(result,sum(h.values()))

print(result)