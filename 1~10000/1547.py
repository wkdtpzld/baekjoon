N=int(input())
cup_list=[1,2,3]

for i in range(N):
    x,y = map(int,input().split())
    xi=cup_list.index(x)
    yi=cup_list.index(y)
    cup_list[xi],cup_list[yi] = cup_list[yi],cup_list[xi]

print(cup_list[0])