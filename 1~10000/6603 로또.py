import sys

m = 6

def dfs(a):
    if len(result) == m:
        for i in result:
            print(i,end=' ')
        print()

    for i in s:
        if i not in result and a < i:
            result.append(i)
            dfs(i)
            result.pop()

while True:
    s = list(map(int,sys.stdin.readline().split()))
    result=[]
    if s[0] == 0 and len(s) == 1:
        break
    s.pop(0)
    len_s= len(s)
    dfs(0)
    print()