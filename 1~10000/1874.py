n=int(input())
cnt=[]
queue=[]
cnt_que=0
for i in range(n):
    a=int(input())
    while cnt_que < a:
        queue.append('+')
        cnt_que += 1
        cnt.append(cnt_que)
    if cnt[-1] == a:
        cnt.pop()
        queue.append('-')
    else:
        print('NO')
        exit()
for i in queue:
    print(i)