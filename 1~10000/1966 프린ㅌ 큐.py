TC=int(input())
for i in range(TC):
    a,b=map(int,input().split())
    a_list=list(map(int,input().split()))
    a_list.sort(reverse=True)
    print(a_list)
