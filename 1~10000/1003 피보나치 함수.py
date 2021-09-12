def fib(n):
    if n == 0:
        return 0
    elif n  == 1 or  n == 2:
        return 1
    a,b=0,1
    for x in range(n-1):
        a,b = b, a+b
    return b

TC=int(input())
for i in range(TC):
    a=int(input())
    for j in range(a):
        print(fib(a))
