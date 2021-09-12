E,S,M=map(int,input().split())
E_s,S_s,M_s=1,1,1
cnt=1
while True:
    if E_s == E and S_s == S and M_s == M:
        print(cnt)
        break
    cnt += 1
    E_s= (E_s+1)%16
    if E_s == 0:
        E_s = 1
    S_s= (S_s+1)%29
    if S_s == 0:
        S_s = 1
    M_s= (M_s+1)%20
    if M_s == 0:
        M_s = 1


