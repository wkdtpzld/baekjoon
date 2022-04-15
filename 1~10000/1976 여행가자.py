n = int(input())
m = int(input())

s = [i for i in range(n+1)]
connect = [-1 for i in range(n)]

def find(k):
    if k != s[k]:
        s[k] = find(s[k])

    return s[k]

def union(x,y):

    x = find(x)
    y = find(y)

    if x < y:
        s[y] = s[x]
    else:
        s[x] = s[y]



for i in range(1,n+1):
    direction = list(map(int,input().split()))

    for j in range(len(direction)):
        if direction[j] == 1:
            union(i,j+1)


f = list(map(int,input().split()))
answer = s[f[0]]

for i in range(1,len(f)):
    if s[f[i]] != answer:
        print("NO")
        exit()

print("YES")