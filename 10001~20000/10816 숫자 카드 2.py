import sys
input = sys.stdin.readline

def binary_search(i,s_n,start,end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if i == s_n[mid]:
        return s_n[start:end+1].count(i)
    elif i < s_n[mid]:
        return binary_search(i,s_n,start,mid-1)
    else:
        return binary_search(i,s_n,mid+1,end)

n = int(input())
s_n=sorted(list(map(int,input().split())))

m = int(input())
s_m=list(map(int,input().split()))

dic={}
for i in s_n:
    start = 0
    end = n - 1
    if i not in dic:
        dic[i] = binary_search(i,s_n,start,end)

for i in s_m:
    if i not in dic:
        print(0,end=" ")
    else:
        print(dic[i],end=" ")