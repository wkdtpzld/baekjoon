from collections import deque

wheel = []

for i in range(4):
    wheel.append(deque(list(map(int, input()))))

TC = int(input())

def dfs(target, direction):

    visited[target] = 1

    if direction == -1:
        if 0 <= target - 2 and visited[target-1] == 0:
            if wheel[target - 1][6] != wheel[target - 2][2]:
                dfs(target - 1, 1)
                wheel[target - 2].appendleft(wheel[target - 2].pop())

        if target < 4 and visited[target+1] == 0:
            if wheel[target - 1][2] != wheel[target][6]:
                dfs(target + 1, 1)
                wheel[target].appendleft(wheel[target].pop())

    if direction == 1:
        if 0 <= target - 2 and visited[target-1] == 0:
            if wheel[target - 1][6] != wheel[target - 2][2]:
                dfs(target - 1, -1)
                wheel[target - 2].append(wheel[target - 2].popleft())

        if target < 4 and visited[target+1] == 0:
            if wheel[target - 1][2] != wheel[target][6]:
                dfs(target + 1, -1)
                wheel[target].append(wheel[target].popleft())

for i in range(TC):
    target, direction = map(int, input().split())
    visited = [0 for _ in range(5)]

    dfs(target, direction)

    if direction == -1:
        wheel[target - 1].append(wheel[target - 1].popleft())
    else:
        wheel[target-1].appendleft(wheel[target-1].pop())

result = 0

for i in range(4):
    if wheel[i][0] == 1:
        result += 2**i

print(result)