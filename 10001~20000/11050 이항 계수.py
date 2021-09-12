def factorial(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans

def factorial_2(n,r):
    return factorial(n) // (factorial(n-r)) // factorial(r)
a,b=map(int,input().split())
print(factorial_2(a,b))