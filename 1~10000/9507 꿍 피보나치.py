import sys

n=int(sys.stdin.readline())
for i in range(n):
    koong = [1,1,2,4]

    num = int(sys.stdin.readline())
    for i in range(4,num+1):
        koong.append(koong[i-1]+koong[i-2]+koong[i-3]+koong[i-4])

    print(koong[num])