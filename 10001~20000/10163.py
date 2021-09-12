import sys
TC=int(input())
paper=[[0]*101 for _ in range(101)]
cnt=[0]*(TC+1)
for i in range(1,TC+1):
    data=list(map(int,sys.stdin.readline().split()))
    for x in range(data[0], data[0]+data[2]):
        for y in range(data[1], data[1]+data[3]):
            paper[x][y] = i

for e in paper:
    for a in e:
        cnt[a] += 1
for e in cnt[1:]:
    print(e)