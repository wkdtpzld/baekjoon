import sys

t = int(input())

for i in range(t):

    n = int(input())
    s = []
    for j in range(2):
        s.append(list(map(int,sys.stdin.readline().split())))

    if len(s[0]) <= 1:
        print(max(s[0][0],s[1][0]))
        continue
    s[0][1] += s[1][0]
    s[1][1] += s[0][0]


    for k in range(2,n):
        s[0][k] += max(s[1][k-1],s[1][k-2])
        s[1][k] += max(s[0][k-1],s[0][k-2])

    print(max(s[0][n-1],s[1][n-1]))