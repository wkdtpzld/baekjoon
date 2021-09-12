n=int(input())
li=sorted(list(map(int,input().split())))
sum_num=[]
for i in range(n):
    if len(sum_num) == 0:
        sum_num.append(li[i])
    else:
        sum_num.append(sum_num[i-1]+li[i])
print(sum(sum_num))