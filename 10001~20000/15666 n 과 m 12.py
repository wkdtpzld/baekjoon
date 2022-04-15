n,m = map(int,input().split())
s=sorted(list(map(int,input().split())))

dic={}
li=[]

def dfs(a):
    if len(li) == m:
        x = ' '.join(map(str,li))
        if x not in dic:
            dic[x] = 1
            print(x)
        return
    for i in range(n):
        if s[i] >= a:
            li.append(s[i])
            dfs(s[i])
            li.pop()

dfs(0)