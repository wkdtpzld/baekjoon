n,k=map(int,input().split())
li=[]
result=[]
for i in range(1,n+1):
    li.append(i)
num=0
for x in range(n):
    num += k-1
    if num >= len(li):

        num = num%len(li)
    result.append(str(li.pop(num)))
print('<',', '.join(result)[:],'>',sep="")
