import sys
input = sys.stdin.readline

n,m = map(int,input().split())

dic={}
li=[]
for i in range(n):
    s = input()
    dic[s] = i+1
    li.append(s)


for i in range(m):
    try:
        search = input()
        print(dic[search])
    except KeyError:
        sys.stdout.write(li[int(search)-1])