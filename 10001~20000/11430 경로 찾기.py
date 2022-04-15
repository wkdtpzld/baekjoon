n = int(input())

s = []
dp = [[0]*n for i in range(n)]
for i in range(n):
    a = list(map(int,input().split()))
    s.append(a)

def search(start):

    queue = []
    queue.append(start)

    while queue:
        x = queue.pop()

        for i in range(n):
            if s[x][i] == 1 and dp[start][i] == 0:
                dp[start][i] = 1
                queue.append(i)


for i in range(n):
    search(i)

for i in dp:
    for j in i:
        print(j,end=" ")
    print()