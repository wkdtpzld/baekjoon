import sys

s=list(map(int,sys.stdin.readline().split()))

one = [1,2,3,4,5]
two = [2,1,2,3,2,4,2,5]
three = [3,3,1,1,2,2,4,4,5,5]

answer=[]
result = [0,0,0]

cnt = 0
for i in s:
    if i == one[cnt]:
        result[0] += 1
    cnt += 1
    if cnt > len(one)-1:
        cnt = 0

cnt = 0

for i in s:
    if i == two[cnt]:
        result[1] += 1
    cnt += 1
    if cnt > len(two) - 1:
        cnt = 0

cnt = 0

for i in s:
    if i == three[cnt]:
        result[2] += 1
    cnt += 1
    if cnt > len(three) - 1:
        cnt = 0

max = 1
for i in range(len(result)):
    if len(answer) == 0:
        if result[i] >= max:
            max = result[i]
            answer.append(i+1)
    else:
        if result[i] > max:
            max = result[i]
            answer.pop()
            answer.append(i+1)
        elif result[i] == max:
            answer.append(i+1)
print(answer)
