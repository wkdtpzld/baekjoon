from math import factorial

N,M,K=map(int,input().split()) # N>=2 1<=M<N 1<=K<=M
res=0
if M == K:
    a=(factorial(N)//((factorial(M))*(factorial(N-M))))
    res +=(1/a)
else:
    if (N-M) < (M-K):
        pass
    else:

        A=(factorial(N-M)//((factorial(M-K))*(factorial((N-M)-(M-K)))))
        B=(factorial(M)//(factorial(K))*(factorial(M-K)))
        a = (factorial(N) // ((factorial(M)) * (factorial(N - M))))
        res += (A*B)/a
print(res)