TC=int(input())
for i in range(TC):
    a,b=map(int,input().split())
    li=list(map(int,input().split()))
    idx=list(range(len(li)))
    idx[b] = 'target'

    order = 0
    while True:
        if li[0] == max(li):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                li.pop(0)
                idx.pop(0)
        else:
            li.append(li.pop(0))
            idx.append(idx.pop(0))