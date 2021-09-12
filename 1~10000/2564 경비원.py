box=list(map(int,input().split()))
TC=int(input())
li=[]
num=[]
cnt=0
for _ in range(TC):
    a,b=map(int,input().split())
    li.append((a,b))
me=list(map(int,input().split()))
# 1:북 2:남 3:서 4:동
for i in li:
    temp=[]
    if me[0] == i[0]:
        temp.append( abs(me[1]-i[1]))
    if me[0] == 2  and i[0] == 3:
        temp.append( box[1]-i[1] + me[1] )
        temp.append( box[1]+box[0]+(box[0]-me[1])+i[1] )
    if me[0] == 1 and i[0] == 3:
        temp.append(me[1] +i[1])
        temp.append(box[1]+box[0]+(box[0]-me[1])+(box[1]-i[1]))
    if me[0] == 2 and i[0] == 4:
        temp.append((box[0]-me[1])+box[1]-i[1])
        temp.append((box[0]+box[1])+me[1]+i[1])
    if me[0] == 1 and i[0] == 4:
        temp.append((box[0]-me[1])+i[1])
        temp.append((box[0]+box[1])+me[1]+(box[1]-i[1]))
    if me[0] == 1 and i[0] == 2:
        temp.append(box[1]+me[1]+i[1])
        temp.append(box[1]+(box[0]-me[1])+(box[0]-i[1]))
    if me[0] == 2 and i[0] == 1:
        temp.append(box[1] + me[1] + i[1])
        temp.append(box[1] + (box[0] - me[1]) + (box[0] - i[1]))
    if me[0] == 3 and i[0] == 4:
        temp.append(box[0] + me[1] + i[1])
        temp.append(box[0]+ (box[1]-me[1]) + (box[1]-i[1]))
    if me[0] == 4 and i[0] == 3:
        temp.append(box[0] + me[1] + i[1])
        temp.append(box[0] + (box[1] - me[1]) + (box[1] - i[1]))
    if me[0] == 3 and i[0] == 1:
        temp.append((box[0] - i[1]) + me[1])
        temp.append((box[0]-i[1]) + box[0] + box[1] + (box[1] - me[1]))
    if me[0] == 4 and i[0] == 1:
        temp.append((box[0] - i[1]) + me[1])
        temp.append((box[0] + box[1]) + i[1] + (box[1] - me[1]))
    if me[0] == 3 and i[0] == 2:
        temp.append(box[1] - me[1] + i[1])
        temp.append(box[1] + box[0] + (box[0] - i[1]) + me[1])
    if me[0] == 4 and i[0] == 2:
        temp.append((box[0] - i[1]) + box[1] - i[1])
        temp.append((box[0] + box[1]) + me[1] + i[1])
    num.append(min(temp))
print(sum(num))
