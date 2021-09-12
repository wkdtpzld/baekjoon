cnt=0
while True:
    cnt += 1
    a=int(input())
    a_li=[]
    if a == 0:
        break
    for i in range(a):
        b=list(map(str,input().split()))
        a_li.append(b)
    for j in a_li:
        for h in range(1,a):
            if j[h] == 'P':
                continue
            elif j[h] == 'N':
                print(f'{a_li[-h][0]} was nasty about {j[0]}')
