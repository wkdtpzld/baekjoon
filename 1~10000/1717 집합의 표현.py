import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n,m = map(int,input().split())

s = [i for i in range(n+1)]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        s[y] = x
    else:
        s[x] = y

def find(k):
    if k != s[k]:
        s[k] = find(s[k])

    return s[k]

for _ in range(m):
    direction,a,b = map(int,input().split())

    if direction == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)