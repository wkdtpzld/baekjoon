n , cnt = int(input()) , 0

a,b,c = [False]*n, [False]*(2*n-1),[False]*(2*n-1)

def dfs(x):
    global cnt
    if x == n:
        cnt += 1
        return

    for i in range(n):
        if not (a[i] or b[x+i] or c[x-i+n-1]):
            a[i] = b[x+i] = c[x-i+n-1] = True
            dfs(x+1)
            a[i] = b[x + i] = c[x - i + n - 1] = False

dfs(0)
print(cnt)