N,K=map(int,input().split())
stack = [i for i in range(1,N+1)]
queue= []
temp = K-1

for i in range(N):
    if len(stack) > temp:
        queue.append(stack.pop(temp))
        temp += K -1
    elif len(stack) <= temp:
        temp %= len(stack)
        queue.append(stack.pop(temp))
        temp += K -1

print('<',end="")
for i in queue:
    if i == queue[-1]:
        print(i, end="")
    else:
        print('%s, '%(i),end="")
print('>')