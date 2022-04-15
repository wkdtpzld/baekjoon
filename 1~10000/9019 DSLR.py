from collections import deque

TC = int(input())

for i in range(TC):
    start,end = map(int,input().split())

    visited=[False]*10000

    queue=deque()
    queue.append([start,""])

    while queue:
        num, path = queue.popleft()
        visited[num] = True
        if num == end:
            print(path)
            break

        num2 = (2*num)%10000
        if not visited[num2]:
            queue.append([num2,path+'D'])
            visited[num2] = True

        num2 = (num-1) % 10000
        if not visited[num2]:
            queue.append([num2, path + 'S'])
            visited[num2] = True

        num2 = (10*num+(num//1000)) % 10000
        if not visited[num2]:
            queue.append([num2, path + 'L'])
            visited[num2] = True

        num2 = (num//10+(num%10)*1000) % 10000
        if not visited[num2]:
            queue.append([num2, path + 'R'])
            visited[num2] = True
