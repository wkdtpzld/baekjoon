from collections import deque
n,k = map(int,input().split())

s=[0]*100001
d=0
queue=deque()
queue.append([n,d])


while queue:
    x,y = queue[0][0],queue[0][1]
    if x == k:
        print(y)
        break
    queue.popleft()
    s[x] = 1
    if (x*2) <= 100000 and s[x*2] == 0:
        queue.append([x*2,y+1])
        s[x*2] = s[x] + 1

    if x - 1 >= 0 and s[x-1] == 0:
        queue.append([x-1,y+1])
        s[x - 1] = s[x] + 1

    if x + 1 <= 100000 and s[x+1] == 0:
        queue.append([x+1,y+1])
        s[x + 1] = s[x] + 1
