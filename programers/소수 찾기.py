from itertools import permutations
import math

def prime_number(n):
    arr = [True]*(n+1)
    for i in range(2,int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while i*j <= n:
                arr[i*j] = False
                j += 1
    return arr



numbers="1239875"
s=[]
for i in numbers:
    s.append(i)

arr=[]
for i in range(1,len(s)+1):
    arr.append(list(permutations(s,i)))

result=[]
for i in arr:
    for j in i:
        a=""
        for k in j:
            a += k
        if int(a) not in result:
            result.append(int(a))

arr2=prime_number(max(result))


cnt = 0
for i in result:
    if i>1 and arr2[i] == True:
        cnt += 1

print(cnt)