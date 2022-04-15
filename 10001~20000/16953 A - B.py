from collections import deque

n,m=map(int,input().split())

queue = deque()
queue.append(n)
answer= {}
answer[n] = 1

while queue:

    x = queue.popleft()

    for i in [x*2,int(str(x)+'1')]:
        if 0 <= i <= m:
            if i not in answer:
                answer[i] = answer[x]+1
                queue.append(i)

try:
    print(answer[m])
except KeyError:
    print(-1)

