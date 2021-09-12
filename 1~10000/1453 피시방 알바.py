# n=int(input())
# a=list(map(int,input().split()))
# arr=0
# for i in range(1,101):
#     cnt=0
#     cnt += a.count(i)
#     if cnt >= 2:
#         arr += a.count(i)-1
# print(arr)

import sys
N = int(input())
mysit = list(map(int,input().split()))

if not len(mysit) == N:
    sys.exit(0)

refcount =0
conter={}
for i in mysit:
    try:
        conter[i] += 1
    except : conter[i] = 1

for i, (key,value) in enumerate(conter.items()):
    if value >= 2:
        refcount += (value -1)
print(refcount)