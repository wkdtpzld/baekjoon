n=list(input())
A='ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ'
result=0
for i in range(len(n)):
    for j in A:
        if n[i] in j:
            result += A.index(j)+3
print(result)

