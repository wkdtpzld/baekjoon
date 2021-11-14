n = int(input())
star = [[' ']*(4*n-3) for i in range(4*n-3)]

def fill_star(n,x,y):
    if n == 1:
        star[x][y] = "*"
        return

    length = 4 * n - 3

    for i in range(length):
        star[y][x+i] = "*"
        star[y+i][x] = "*"
        star[y+length-1][x+i] = "*"
        star[y+i][x+length-1] = "*"

    fill_star(n-1,x+2,y+2)

fill_star(n,0,0)
for i in range(len(star)):
    for j in range(len(star)):
        print(star[i][j],end="")
    print()