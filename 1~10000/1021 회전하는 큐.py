from collections import deque
n,m=map(int,input().split())
n_li=deque([i for i in range(1,n+1)])
m_li=list(map(int,input().split()))
cnt=0
li=[]
while len(m_li) != 0:
    a=n_li.index(m_li[0])
    b=len(n_li)-a
    if n_li[0] == m_li[0]:
        n_li.popleft()
        m_li.pop(0)
    elif n_li[0] != m_li[0] and a>b:
        n_li.appendleft(n_li.pop())
        cnt +=1

    elif n_li[0] != m_li[0] and a<=b:
        n_li.append(n_li.popleft())
        cnt +=1

print(cnt)