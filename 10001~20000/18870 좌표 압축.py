n=int(input())
s=list(map(int,input().split()))
ss=sorted(list(set(s)))

dic={ss[i] : i for i in range(len(ss))}


for i in s:
    print(dic[i],end=" ")