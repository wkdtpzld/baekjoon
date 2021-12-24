from collections import deque

TC = int(input())

Flag = False


for i in range(TC):
    order=input()
    length=int(input())
    a = input()[1:-1].split(",")

    if a[0] != '':
        a = deque(a)
    else:
        a = deque()

    direction_Flag = True

    for p in order:

        if p == 'R':
            if direction_Flag == True:
                direction_Flag = False
            elif direction_Flag == False:
                direction_Flag = True
        elif p == 'D':
            if len(a) == 0:
                print("error")
                Flag = True
                break

            if direction_Flag == True:
                a.popleft()
            elif direction_Flag == False:
                a.pop()

    if order.count('R') % 2 != 0:
        a.reverse()

    if Flag == False:
        print("[",end="")
        for i in range(len(a)):
            print(a[i],end="")
            if i != len(a)-1:
                print(",",end="")
        print("]")
    Flag = False