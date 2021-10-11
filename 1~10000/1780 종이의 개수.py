import sys

n=int(input())
s=[list(map(int,sys.stdin.readline().split())) for i in range(n)]

minus=0
zero=0
one=0

def search(x,y,n):

    global minus,zero,one

    check=s[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if s[i][j] != check:
                for k in range(3):
                    for h in range(3):
                        search(x+k*(n//3),y+h*(n//3),n//3)
                return

    if check == -1:
        minus += 1
    elif check == 0:
        zero += 1
    elif check == 1:
        one += 1

search(0,0,n)
print(minus)
print(zero)
print(one)
