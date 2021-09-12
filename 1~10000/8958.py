n=int(input())
for i in range(n):
    li=list(input())
    cnt=0
    x_result=1
    for j in li:
        if j == 'O':
            cnt += x_result
            x_result += 1
        else:
            cnt += 0
            x_result = 1
    print(cnt)