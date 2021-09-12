N=int(input())
result=0
for i in range(N):
    a=list(input())
    for j in range(len(a)):
        if j != len(a)-1:
            if a[j] == a[j+1] :
                pass
            elif a[j] in a[j+1:]:
                break
        else:
            result +=1
print(result)