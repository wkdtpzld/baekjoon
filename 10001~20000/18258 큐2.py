import sys
import collections
TC=int(sys.stdin.readline())
dq=collections.deque()

for i in range(TC):
    order=list(sys.stdin.readline().split())

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
    if 'push' == order[0]:
        dq.append(order[1])
    if 'pop' == order[0]:
        try:
            print(dq.popleft())
        except IndexError:
            print(-1)