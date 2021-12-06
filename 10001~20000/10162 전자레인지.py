t = int(input())

s = [300,60,10]
result=[0,0,0]
if t > 10:
    if t % 10 != 0:
        print(-1)
        exit()

for i in range(3):
    if t >= s[i]:
        result[i] += (t//s[i])
        t -= result[i]*s[i]

if t == 0:
    for i in result:
        print(i,end=" ")
else:
    print(-1)
