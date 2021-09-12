TC=int(input())
li=[list(map(int,input().split())) for _ in range(TC)]

arr=[[0]*TC for _ in range(TC)]
for x in range(TC):
    for grade in range(5):
        for student in range(TC):
            if student == x:
                continue
            if li[x][grade] == li[student][grade]:
                arr[x][student] = 1

result=[]
for o in range(TC):
    asdasdasd=0
    for u in range(TC):
        if arr[o][u] == 1:
            asdasdasd += 1
    result.append(asdasdasd)
print(result.index(max(result))+1)
