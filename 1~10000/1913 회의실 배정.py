import sys

n=int(input())
li=[list(map(int,sys.stdin.readline().split())) for i in range(n)]
li.sort(key= lambda x: (x[1],x[0]))
a,s=0,0
for i,j in li:
    if a <= i:
        s += 1
        a = j
print(s)