# x,y,w,h=map(str,input().split())
# A=int(w)-int(x)
# B=int(h)-int(y)
# if A<B:
#     print(A)
# else:
#     print(B)

x,y,w,h=map(int,input().split())
print(min(x,y,w-x,h-y))