n = int(input())

star = [[' ' for _ in range(n)] for i in range(n)]


def solution(n,x,y):
    if n == 1:
        star[x][y] = "*"
    else:
        next_n = n//3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    solution(next_n, x + dx * next_n, y + dy * next_n)

solution(n,0,0)


for i in range(n):
    for j in range(n):
        print(star[i][j],end="")
    print()