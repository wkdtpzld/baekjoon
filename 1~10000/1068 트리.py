n = int(input())
s = list(map(int,input().split()))
remove = int(input())

cnt = 0

def dfs(x,arr):
    arr[x] = -2
    for i in range(n):
        if x == arr[i]:
            dfs(i,arr)

dfs(remove,s)
for i in range(n):
    if s[i] != -2 and i not in s:
        cnt += 1

print(cnt)