n=int(input())
li=[]
for i in range(n):
    li.append(list(map(str,input().split())))
li.sort()
print(li)