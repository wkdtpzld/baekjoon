# branchorama 라는 나무 가지가 spltting factor 의 가지
# 첫번째는 나무의 나이 2a는 차례대로 splitting factor와 가지치기 수
while True:
    list_t=list(map(int,input().split()))
    if list_t[0] == 0:
        break
    n=1
    for i in range(list_t[0]): # 2 3 0 2 0
        a=list_t[2*i + 1] # 5
        b=list_t[2*i + 2] # 6
        n=n*a - b
    print(n)
