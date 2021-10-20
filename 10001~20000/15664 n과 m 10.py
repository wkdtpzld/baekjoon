n,m=map(int,input().split())
s=sorted(list(map(int,input().split())))

li=[]
dic={}

def dfs(a):
    if len(li) == m:
        x = ' '.join(map(str,li))
        if x not in dic:
            print(x)
            dic[x] = 1
        return
    for i in range(n):
        if i > a:
            li.append(s[i])
            dfs(i)
            li.pop()

dfs(-1)