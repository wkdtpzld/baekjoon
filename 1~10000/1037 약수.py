n=int(input())
arr=list(map(int,input().split()))
copy_arr=arr

def gcd(a,b):
    while b != 0:
        a,b =b,a%b
    return a

GCDarr=arr[0]
LCMarr=arr[0]
for i in range(len(arr)):
    GCDarr=gcd(LCMarr,arr[i])
    LCMarr=LCMarr * arr[i] // GCDarr

if LCMarr in copy_arr:
    print(LCMarr * min(copy_arr))
else:
    print(LCMarr)