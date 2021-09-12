N,L,D = map(int,input().split())
L_len=0
D_len=0
i=0
while i*D < N*(L+5)-5:
    if L <= i*D %(L+5) <= L+4:
        L_len=i*D
        D_len=1
        break
    i += 1
print(L_len if D_len else ((N*(L+5)-5)//D+1))