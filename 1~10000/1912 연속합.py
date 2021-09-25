import sys

n =int(input())
s =list(map(int,sys.stdin.readline().split()))

for i in range(1,n):
    s[i] = (max(s[i],s[i-1]+s[i]))

print(s)