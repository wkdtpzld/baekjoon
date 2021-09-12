# n=1260
# cnt=0
# lst=[500,100,50,10]
#
# for i in lst:
#     cnt += n//i
#     n  %= i
#
# print(cnt)

# n,k=map(int,input().split())
# result=0
# while True:
#     target=(n//k)*k
#     result += (n-target)
#     n=target
#
#     if n<k:
#         break
#
#     result += 1
#     n = n//k
#
# result += (n-1)
# print(result)

# data=input()
# result= int(data[0])
# for i in range(1,len(data)):
#     num=int(data[i])
#     if num<=1 or result<=1:
#         result += num
#     else:
#         result *= num
# print(result)

N = int(input())
dp = [0, 0, 1, 1]

for i in range(4, N+1 ):
    dp.append(dp[i-1] + 1)
    if i % 2 == 0:    dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:    dp[i] = min(dp[i // 3] + 1, dp[i])

print(dp[N])
#
#
#
# a=int(input())
# b=[5,3]
# c=0
#
# for i in b:
#     c += a//i
#     a = a%i
#
#
# if a != 0 :
#     print('-1')
# else:
#     print(c)
