n=int(input())
n_count=list(map(int,input().split()))
y=0
m=0
for i in n_count:
    y += i // 30 * 10 + 10
    m += i // 60 * 15 + 15
if m>y:
    print('Y %d'% y)
elif m<y:
    print('M %d'% m)
else:
    print('Y M %d'% y)