n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))

visited=[0 for i in range(n)]
result=[]

min_result=1000000000

def dfs(idx,cnt):
    global  min_result

    if cnt == (n//2):
        start,link = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] == 1 and visited[j] == 1:
                    start += matrix[i][j]
                elif visited[i] == 0 and visited[j] == 0:
                    link += matrix[i][j]
        min_result = min(min_result, abs(start-link))


    for i in range(idx,n):
        if visited[i] == 0:
            visited[i] = 1
            dfs(i+1 , cnt + 1)
            visited[i] = 0

dfs(0,0)
print(min_result)

