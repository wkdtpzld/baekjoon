import sys
n=int(input())
li=[]
count=[]
for _ in range(n):
    li.append(list((map(int,input().split()))))
for i in range(len(li)):
    cnt=1
    for j in range(len(li)):
        if i == j :
            continue
        else:
            if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                cnt += 1
    count.append(cnt)
for h in count:
    sys.stdout.write(str(h)+' ')