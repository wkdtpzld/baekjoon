import sys

sys.setrecursionlimit(10000000)

n = int(input())
tree=[[] for _ in range(n+1)]

Parent=[0 for _ in range(n+1)]

for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)



def dfs(start, tree, Parent):
    for i in tree[start]:
        if Parent[i] == 0:
            Parent[i] = start
            dfs(i, tree, Parent)

dfs(1,tree,Parent)

for i in range(2,n+1):
    print(Parent[i])