n,m=map(int,input().split())
hole = list(map(int,input().split()))
hole.sort()

end = hole[0] + m - 0.5
cnt = 1

for i in hole:
    if end >= i:
        continue
    else:
        cnt += 1
        end = i + m - 0.5
print(cnt)

