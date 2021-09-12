import math
A,B,N=map(int,input().split())
arr=N-B
AB=A-B
print(math.ceil(arr/AB))
