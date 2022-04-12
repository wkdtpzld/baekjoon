n = int(input())
s = list(map(int,input().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1,n):
    while stack and s[stack[-1]] < s[i] :
        answer[stack.pop()] = s[i]
    stack.append(i)


print(*answer)