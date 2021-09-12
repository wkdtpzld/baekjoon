TC=int(input())
a_li=[]
for i in range(TC):
    a=input()
    a_1=a[0]
    a_li.append(a_1)
a_sort=set(a_li)
a_lis=[]

for j in a_sort:
    if a_li.count(j) >= 5:
        a_lis.append(j)
a_lis.sort()
if len(a_lis) == 0:
    print('PREDAJA')
else:
    print(''.join(a_lis))
