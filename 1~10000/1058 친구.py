n=int(input())

s=[]

for i in range(n):
    s.append(list(input()))

visit=[[0 for i in range(n)] for _ in range(n)]


for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if s[j][k] =="Y" or (s[j][i]=='Y' and s[i][k]=="Y"):
                visit[j][k] = 1

result = 0

for i in visit:
    result = max(result,sum(i))
print(result)