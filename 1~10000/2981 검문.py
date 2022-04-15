import math

n = int(input())

s=[]

answer = []
gcd = 0
for i in range(n):
    s.append(int(input()))
    if i == 1:
        gcd = abs(s[1]-s[0])

    gcd = math.gcd(abs(s[i]-s[i-1]),gcd)

gcd_a = int(gcd ** 0.5)

for i in range(2,gcd_a+1):
    if gcd % i == 0:
        answer.append(i)
        answer.append(gcd // i)

answer.append(gcd)

answer = list(set(answer))

answer.sort()

print(' '.join(map(str,answer)))