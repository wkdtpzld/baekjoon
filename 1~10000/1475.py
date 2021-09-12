numbers=list(input())
number=['0','1','2','3','4','5','6','7','8','9']
cnt=[0]*10

sixnine=0

for i in range(10):
    cnt[i] = numbers.count(number[i])
    if i == 6 or i == 9:
        sixnine += cnt[i]
        cnt[i] = 0

big=max(cnt)

if sixnine%2 ==0:
    sixnine //= 2
else:
    sixnine = sixnine //2 + 1

print(max(sixnine,big))