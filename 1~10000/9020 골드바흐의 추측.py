import math
import sys
input = sys.stdin.readline

T = int(input())

def prime_number(n):

    array = [0 for i in range(n+1)]

    for i in range(2,int(math.sqrt(n))+1):
        if array[i] == 0:
            j = 2
            while i * j <= n:
                array[i*j] = 1
                j += 1

    return array


s = prime_number(10000)

for i in range(T):
    n = int(input())

    n2 = n // 2

    for j in range(n2,1,-1):
        if s[n-j] == 0 and s[j] == 0:
            print(j,n-j)
            break