from collections import deque

s = [-1 for i in range(101)]

visited=[i for i in range(101)]

n,m = map(int,input().split())

for i in range(n):
    a,b=map(int,input().split())

    visited[a] = b

for i in range(m):
    a,b=map(int,input().split())

    visited[a] = b

queue = deque()
queue.append(1)

s[1] = 0

while queue:
    x = queue.popleft()

    for i in range(1,7):
        y = x+i
        if (y>100):
            continue
        y = visited[y]
        if (s[y] == -1 or s[y]>s[x]+1):
            s[y] = s[x]+1
            queue.append(y)

print(s[100])
