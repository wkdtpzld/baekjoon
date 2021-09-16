import math


def is_prime_number(n,s):
    arr = [True for i in range(n+1)]

    for i in range(2,int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while i * j <= n:
                arr[i*j] = False
                j += 1
    for j in range(s+1):
        arr[j] = False

    return [i for i in range(2, n+1) if arr[i]]



while True:
    s = int(input())
    if s == 0:
        break
    else:
        n = s*2
        print(len(is_prime_number(n,s)))