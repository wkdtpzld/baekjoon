n,x,y = map(int,input().split())
cnt = 0

while n != 0:
    s = (2 ** n) // 2
    if x < s and y < s :
        pass
    elif x < s and y >= s:
        cnt += s**2
        y -= s
    elif x >= s and y < s:
        cnt += s ** 2 * 2
        x -= s
    elif x >= s and y >= s:
        cnt += s ** 2 * 3
        x -= s
        y -= s
    n -= 1

print(cnt)
