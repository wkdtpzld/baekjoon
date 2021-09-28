TC=int(input())
for i in range(TC):
    A,B = map(int,input().split())
    n = B - A
    cnt = 0
    move = 1
    move_sum = 0

    while move_sum < n:
        cnt += 1
        move_sum += move
        if cnt % 2 == 0:
            move += 1

    print(cnt)