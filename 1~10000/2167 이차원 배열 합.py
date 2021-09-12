n,m=map(int,input().split())
li=[]
for i in range(n):
    li.append(list(map(int,input().split())))
K=int(input())

for _ in range(K):
    K_li = []
    K_li.append(list(map(int,input().split())))
    i=K_li[0][0]-1
    j=K_li[0][1]-1
    x=K_li[0][2]-1
    y=K_li[0][3]-1
    cnt=0
    if i < x:
        for arr in range(i,x+1):
            cnt += sum((li[arr][j:y+1]))
        print(cnt)
    elif i == x and j == y:
        print((li[x][y]))
    elif i == x and j != y:
        print(sum(li[i][j:y+1]))