import math
n,m=map(int,input().split())
n_li=[True for i in range(n+1)]
result=[]
for i in range(2,int(math.sqrt(n))+1):
    if n_li[i] == True:
        n_li[i] = False
        result.append(i)
        k=2

        while i*k <= n:
            if n_li[i*k] == True:
                n_li[i*k] = False
                result.append(i*k)
            k += 1
for j in range(2,n+1):
    if n_li[j] == True:
        result.append(j)
print(result[m-1])