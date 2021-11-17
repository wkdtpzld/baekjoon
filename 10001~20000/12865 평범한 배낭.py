import sys
input = sys.stdin.readline


n, k =map(int,input().split())

s=[[0]*(k+1) for i in range(n+1)]


v2 = [[0,0]]

for i in range(n):
    weight, value =map(int,input().split())
    v2.append([weight,value])

for i in range(1,n+1):
    for j in range(1,k+1):
        w = v2[i][0]
        v = v2[i][1]

        if j < w:
            s[i][j] = s[i-1][j]
        else:
            s[i][j] = max(s[i-1][j], s[i-1][j-w]+v)

print(s[n][k])

# def knapsack(bag, n):
#     if bag == 0 or n == 0:
#         return 0
#     if s[n-1][0] > bag:
#         return knapsack(bag,n-1)
#     else:
#         return max(s[n-1][1] + knapsack(bag-s[n-1][0],n-1),knapsack(bag, n-1))
#
# print(knapsack(k,n))

