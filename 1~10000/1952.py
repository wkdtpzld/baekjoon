N,L,D =map(int,input().split()) # N=곡 수 L=곡 길이 D=전화벨
i=1
a=0
b=0
while i*D<=N*(L+5)-5:
    if L<=i*D%(L+5)<=L+4:   # 2 , 5 , 4  16이 5~9가 되도록 만들기
        a=i*D
        break
    i += 1
if a != 0:
    print(a)
else:
    print(int((N*(L+5)-5)/D+1)*D)

