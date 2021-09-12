box=list(map(int,input().split()))
temp_x=[]
temp_y=[]
TC=int(input())
li=[]
for i in range(TC):
    a,b=map(int,input().split())
    li.append((a,b))

for x in li:

    if x[0] == 0:
        temp_y.append(max(box[1]-x[1],x[1]))
    if x[0] == 1:
        temp_x.append(max(box[0]-x[1],x[1]))
