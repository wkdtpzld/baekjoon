def prime_num(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

N,M=map(int,input().split())
num=[]
for i in range(N,M+1):
    if prime_num(i) == True:
        num.append(i)
for i in num:
    print(i)