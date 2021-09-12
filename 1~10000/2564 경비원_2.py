N=int(input())

li=list(map(int,input().split()))
line=[]
for i in range(N):
    line.insert(i-li[i],i+1)

for i in line:
    print(i,end=" ")