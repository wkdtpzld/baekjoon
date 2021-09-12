# 곡의 수 =N 모든 노래의 길이 =L 노래 사이에는 5초의 공백구간
# D초에 한번씩 전화벨이 울림. 한 번 울릴떄 1초동안 울림.
N,L,D=map(int,input().split())
N_time=0
N_times=[]
D_time=0
D_times=[]
for i in range(N):
    N_time += L
    for j in range(5):
        N_time += 1
        N_times.append(N_time)

while True:
    D_time += D
    D_times.append(D)
    D_times.append(D+1)
    if D_time > 1000:
        ND = list(set(N_times).intersection(D_times))
        print(min(ND))
        break
    D +=D




#         print(D_time)
#     elif D_time>N_time:
#         print(D_time)
#     elif D_time>1000:
#         break



    # if N_time == D and N_time == D+1:
