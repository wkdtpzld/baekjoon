import sys
n,m=map(int,sys.stdin.readline().split())
li=[[] for _ in range(n+1)]


for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    li[b].append(a)


def dfs(x,visited):
    visited += [x]
    for i in range(len(li[x])):
        if li[x][i] not in visited:
            dfs(li[x][i],visited)
    return visited

result=[]
for i in range(0,n+1):
    result.append(len(dfs(i,[])))

for x in range(len(result)):
    if result[x] == max(result):
        sys.stdout.write(str(x)+' ')