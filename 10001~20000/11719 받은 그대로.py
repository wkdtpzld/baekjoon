# def binary_search(a, x):
#     start = 0
#     end = len(a)-1
#
#     while start <= end:
#         mid = (start + end) //2
#         if x == a[mid]:
#             return mid
#         elif x > a[mid]:
#             start = mid +1
#         else:
#             end = mid - 1
#
#     return -1

K,N=map(int,input().split())
k_li=[]
for _ in range(K):
    k_li.append(int(input()))
k_li.sort()
start=1
end=max(k_li)

while start <= end:
    cnt=0
    mid = (start + end) //2
    for i in range(K):
        cnt += k_li[i]//mid
    if cnt>=N:
        start = mid +1
    else:
        end = mid -1
print(end)

K,N=map(int,input().split())
k_li=[]
for _ in range(K):
    k_li.append(int(input()))
k_li.sort()
start=1
end=max(k_li)

while start <= end:
    cnt=0
    mid = (start + end) //2
    for i in range(K):
        cnt += k_li[i]//mid
    if cnt == N:
        print(mid)
        break
    elif cnt < N:
        end = mid-1
    else:
        start = mid +1