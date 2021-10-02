n=int(input())

for i in range(n):
    flag = True
    stack = []
    s = list(input())
    for j in s:
        if j == "(":
            stack.append(j)
        elif j == ")":
            try:
                stack.pop()
            except IndexError:
                flag = False
                break
    if len(stack) == 0 and flag == True:
        print("YES")
    else:
        print("NO")