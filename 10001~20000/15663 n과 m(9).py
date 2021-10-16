n,m = map(int,input().split())
s = sorted(list(map(int,input().split())))

li=[]
result=[]
dic={}

check=[0]*n

def dfs():
    if len(li) == m:
        line = ' '.join(map(str,li))
        if line not in dic:
            dic[line] = 1
            print(line)
        return
    for i in range(n):
        if check[i] == 1:
            continue

        li.append(s[i])
        check[i] = 1
        dfs()
        li.pop()
        check[i] = 0

dfs()
print(dic)