n = int(input())
s=[]
for d in range(n):
    s.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(s[i])):
        if j == 0:
            s[i][j] = s[i][j]+s[i-1][j]
        elif j == len(s[i])-1:
            s[i][j] = s[i][j] + s[i-1][j-1]
        else:
            s[i][j] = max(s[i-1][j-1],s[i-1][j])+s[i][j]

print(max(s[-1]))