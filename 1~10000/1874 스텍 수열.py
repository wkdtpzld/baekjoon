n = int(input())

s = []
op = []
cnt = 1
flag = True


for i in range(n):
    num = int(input())
    while cnt <= num:
        s.append(cnt)
        op.append('+')
        cnt += 1
    if s[-1] == num:
        s.pop()
        op.append('-')
    else:
        flag = False

if flag == False:
    print("NO")
else:
    print('\n'.join(op))