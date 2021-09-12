import sys
n=int(input())
std=[]
for i in range(n):
    a,b,c,d=map(str,sys.stdin.readline().split())
    b = int(b)
    c = int(c)
    d = int(d)
    std.append((a,b,c,d))

std.sort(key=lambda y: (-(y[1]),(y[2]),-(y[3]),y[0]))

for result in std:
    sys.stdout.write(str(result[0]+'\n'))

