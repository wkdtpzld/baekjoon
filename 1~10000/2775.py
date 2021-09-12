TC=int(input())
for _ in range(TC):
    a=int(input())
    b=int(input())
    number=[]
    for i in range(a):
        temp = []
        for j in range(b):
            if i == 0:
                temp.append(j+1)
            else:
                temp.append(sum(number[i-1][:j+1]))
        number.append(temp)
    print(sum(number[a-1]))

