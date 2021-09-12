def GCD(a,b):
    while b>0:
        a , b = b, a%b
    return a


n=int(input())
for i in range(n):
    result=[]
    order=list(map(int,input().split()))

    for i in range(1,len(order)):
        for j in range(1,len(order)):
            if i >= j:
                continue
            else:
                result.append(GCD(order[i],order[j]))
    print(sum(result))
