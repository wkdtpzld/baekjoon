n = int(input())
s = input()

li = [0] * n

for i in range(n):
    li[i] = int(input())

stack = []

for i in s:
    if 'A' <= i <= 'Z':
        stack.append(li[ord(i) - ord('A')])
    else:
        p2 = stack.pop()
        p1 = stack.pop()

        if i == '+':
            stack.append(p1+p2)
        elif i == '-':
            stack.append(p1-p2)
        elif i == '*':
            stack.append(p1*p2)
        elif i == '/':
            stack.append(p1/p2)

print('%.2f' %stack[0])