import sys

def bfs():
    global size,size_cnt

    answer = 0

    shark = []
    feed = [[] for i in range(6)]

    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                shark.append([i, j])
            if 1 <= board[i][j] <= 6:
                feed[board[i][j] - 1].append([i, j])

    visited = [[0] * n for i in range(n)]
    visited[shark[0][0]][shark[0][1]] = 1

    while shark:
        x, y = shark.pop(0)

        for i in range(4):
            dx, dy = x + nx[i], y + ny[i]

            if 0 <= dx < n and 0 <= dy < n:
                if board[dx][dy] <= size and visited[dx][dy] == 0:
                    visited[dx][dy] = visited[x][y] + 1
                    shark.append([dx, dy])

    check = [INF, [INF,INF]]
    for i in range(size - 1):
        for j in feed[i]:
            if visited[j[0]][j[1]] < check[0]:
                check[0] = visited[j[0]][j[1]]
                check[1] = j
            if visited[j[0]][j[1]] == check[0]:
                if j[0] < check[1][0]:
                    check[1] = j
                if j[0] == check[1][0]:
                    if j[1] < check[1][1]:
                        check[1] = j

    if check[0] != INF:
        answer += check[0]
        board[check[1][0]][check[1][1]] = 9
        size_cnt += 1
        if size_cnt == size:
            size_cnt = 0
            size += 1
        if size > 7:
            size = 7

    return answer


INF = sys.maxsize
n = int(input())

nx,ny=[-1,0,1,0],[0,-1,0,1]

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))

size = 2
size_cnt = 0

result = 0
while True:
    try:
        result += bfs()-1
    except IndexError:
        break
print(result+1)