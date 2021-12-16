from collections import deque
import sys

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
sys.setrecursionlimit(10**9)

n = int(input())

board = [[0]*(n+1) for i in range(n+1)]

apple = int(input())

for i in range(apple):
    a,b = map(int,input().split())
    board[a][b] = 1

snake = 1
board[1][1] = 2

m=int(input())

turn = deque([])
for i in range(m):
    s = list(input().split())
    turn.append(s)

cnt = 0
last = deque([[1,1]])

def snake_board(x,y,snake):

    global cnt

    while True:
        x, y = x + direction[snake][0], y + direction[snake][1]

        if 0 < x <= n and 0 < y <= n and board[x][y] != 2:
            if not board[x][y] == 1:
                tx, ty = last.popleft()
                board[tx][ty] = 0
            board[x][y] = 2
            last.append([x,y])
            cnt += 1

            if turn:
                if cnt == int(turn[0][0]):
                    if turn[0][1] == "D":
                        snake = (snake + 1) % 4

                    elif turn[0][1] == "L":
                        snake = (snake - 1) % 4
                    turn.popleft()


        else:
            return cnt

print(snake_board(1,1,1)+1)
