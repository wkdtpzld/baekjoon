import sys
TC=int(sys.stdin.readline())
stack=[]

for i in range(TC):
    order=list(sys.stdin.readline().split())

    if 'size' == order[0]:
        print(len(stack))
    if 'empty' == order[0]:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if 'push' == order[0]:
        stack.append(order[1])
    if 'pop' == order[0]:
        try:
            print(stack.pop())
        except IndexError:
            print(-1)
    if 'top' == order[0]:
        try:
            print(stack[-1])
        except IndexError:
            print(-1)
