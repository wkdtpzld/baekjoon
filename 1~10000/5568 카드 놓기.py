n = int(input())
k = int(input())

s=[]

for i in range(n):
    s.append(int(input()))

check = [0] * n
li = []
se = set()

def dfs(depth):
    if depth == k:
        se.add("".join(map(str, li)))
        return

    for i in range(n):
        if check[i] == 1:
            continue
        li.append(s[i])
        check[i] = 1
        dfs(depth + 1)
        li.pop()
        check[i] = 0

dfs(0)

print(len(se))
#
# result=[]
# dic = {}
# li = []
# a = ""
# def dfs():
#     if len(li) == k:
#         a = ""
#         for i in li:
#             a += s[i]
#         dic[a] = 1
#
#     for i in range(n):
#         if i not in li:
#            li.append(i)
#
#            dfs()
#            li.pop()
#
# dfs()
# print(len(dic))