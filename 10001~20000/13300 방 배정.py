TC,K=map(int,input().split())
room=[0]*13
result=0
for i in range(TC):
    s,grade=map(int,input().split())
    if s == 0:
        room[grade] += 1
    elif s == 1:
        room[grade+6] += 1

for i in room:
    if i == 0:
        pass
    elif i <= K and i > 0:
        result += 1
    elif i > K:
        if i%K == 0:
            result += (i//K)
        else:
            result += (i//K)+1
print(result)
