import sys

n,m = map(int,input().split())
li=list(map(int,sys.stdin.readline().split()))
li.sort()
result=[]

def DFS(a):
    if len(result) == m:
        print(' '.join(map(str,result)))
    for i in li:
        if i not in result and a < i:
            result.append(i)
            DFS(i)
            result.pop()
DFS(0)
