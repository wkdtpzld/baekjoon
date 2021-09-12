TC=int(input())
li=[list(map(int,input().split())) for _ in range(TC)]

arr=[[0]*5 for _ in range(TC)]
for x in range(TC):
    for grade in range(5):
        li_1=[]
        for student in range(TC):
            if student == x:
                continue
            elif li[x][grade] == li[student][grade]:
                li_1.append(student)
        p