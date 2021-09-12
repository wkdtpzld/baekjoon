n=int(input())
cnt=0
a=[]
while cnt <= n:
    if cnt == 0:
        a.append(0)
    elif cnt == 1:
        a.append(1)
    else:
        a.append(a[cnt-1]+a[cnt-2])
    cnt += 1
print(a[n])

