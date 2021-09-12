import sys

TC = int(input())
result = [False for i in range(21)]
for i in range(TC):
    order = list(sys.stdin.readline().split())
    if order[0] == 'add':
        result[int(order[1])] = True
    if order[0] == 'remove':
        try:
            result[int(order[1])] = False
        except ValueError:
            continue
    if order[0] == 'check':
        if result[int(order[1])] == True:
            print(1)
        else:
            print(0)
    if order[0] == 'toggle':
        if result[int(order[1])] == True:
            result[int(order[1])] = False
        else:
            result[int(order[1])] = True
    if order[0] == 'all':
        result = [True for i in range(21)]
    if order[0] == 'empty':
        result = [False for i in range(21)]
