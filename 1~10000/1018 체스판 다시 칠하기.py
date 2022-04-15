a,b=map(int,input().split())
a_li=[]
b_li=[]

for _ in range(a):
    a_li.append(input())
for i in range(a-7):
    for j in range(b-7):
        f_w=0
        f_b=0
        for h in range(i,i+8):
            for h_1 in range(j,j+8):
                if (h + h_1)%2 == 0:
                    if a_li[h][h_1] != 'W':
                        f_w += 1
                    if a_li[h][h_1] != 'B':
                        f_b += 1
                else:
                    if a_li[h][h_1] != 'B':
                        f_w += 1
                    if a_li[h][h_1] != 'W':
                        f_b += 1
        b_li.append(f_b)
        b_li.append(f_w)
print(min(b_li))