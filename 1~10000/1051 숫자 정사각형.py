n,m=map(int,input().split())
result=[]
box=[ list(input()) for i in range(n)]
min_num=min(n,m)
for i in range(n):
    for j in range(m):
        for k in range(min_num):
            if (i+k)<n and (j+k)<m and box[i][j] == box[i][j+k] == box[i+k][j] == box[i+k][j+k]:
                result.append((k+1)**2)
print(max(result))