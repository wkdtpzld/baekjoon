from collections import deque
import sys
TC=int(sys.stdin.readline())
dq=deque()

for i in range(TC):
    order=list(sys.stdin.readline().split())

    if 'push_back' in order[0]:
        dq.append(order[1])
    if 'push_front' in order[0]:
        dq.appendleft(order[1])
    if 'front' == order[0]:
        try:
            print(dq[0])
        except IndexError:
            print(-1)
    if 'back' == order[0]:
        try:
            print(dq[-1])
        except IndexError:
            print(-1)
    if 'size' == order[0]:
        print(len(dq))
    if 'empty' == order[0]:
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    if 'pop_front' == order[0]:
        try:
            print(dq.popleft())
        except IndexError:
            print(-1)
    if 'pop_back' == order[0]:
        try:
            print(dq.pop())
        except:
            print(-1)