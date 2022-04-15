import sys
input = sys.stdin.readline

n,m=map(int,input().split())

user={}
for i in range(n):
    id,pw = map(str,input().split())
    user[id] = pw


for i in range(m):
    a = input().split()
    sys.stdout.write(user[a[0]]+"\n")



