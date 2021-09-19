import math

n,m=map(int,input().split())

def factorial(n,m):
    return math.factorial(n) // (math.factorial(m)*math.factorial(n-m))

print(factorial(n,m))