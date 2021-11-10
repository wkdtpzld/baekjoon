n,m = map(int,input().split())

a = []
for i in range(n):
    a.append(list(map(int,input())))

b = []
for i in range(n):
    b.append(list(map(int,input())))

def change(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            a[i][j] = 1-a[i][j]

cnt = 0

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            change(i,j)
            cnt += 1

flag=True

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            flag=False
if flag==False:
    print(-1)
else:
    print(cnt)