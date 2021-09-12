import sys
n= int(input())

check_li=[0]*10001
for i in range(n):
    int_input=int(sys.stdin.readline())

    check_li[int_input] = check_li[int_input] + 1
for i in range(10001):
    if check_li[i] != 0:
        for j in range(check_li[i]):
            print(i)