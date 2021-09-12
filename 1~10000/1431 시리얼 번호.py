n = int(input())

def sum_num(tmp):
    result = 0
    for i in tmp:
        if i.isdigit():
            result += int(i)
    return  result

li=[]
for i in range(n):
    a = list(input())
    li.append(a)

li.sort(key=lambda x: (len(x), sum_num(x),x))

for i in li:
    for j in i:
        print(j,end='')
    print()

