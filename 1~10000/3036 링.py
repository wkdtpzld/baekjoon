import sys
n= int(input())
rings = list(map(int,sys.stdin.readline().split()))

def gcd(a,b):
    while b>0:
        a ,b = b , a % b
    return a

for i in range(1,(len(rings))):
    print(f'{rings[0]//(gcd(rings[0],rings[i]))}/{rings[i]//(gcd(rings[0],rings[i]))}')