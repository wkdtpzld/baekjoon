n = int(input())

s = [int(input()) for i in range(n)]

def gcd(a,b):

    while b > 0:
        a,b = b, a%b
    return a

