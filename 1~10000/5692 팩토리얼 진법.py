import math
import sys

input = sys.stdin.readline

while True:
    n = input().split()


    length = len(n[0])

    if n[0] =='0':
        break

    sum = 0
    for i in range(length):
        sum += int(n[0][i])*math.factorial(length)
        length -= 1
    print(sum)