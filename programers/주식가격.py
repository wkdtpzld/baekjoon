n=int(input())

prices = list(map(int,input().split()))

answer=[0]*(len(prices))
stack = []

for t,i in enumerate(prices):
    while stack and stack[-1][1] > i:
        v = stack.pop()
        answer[v[0]] = t - v[0]

    stack.append([t,i])

while stack:
    time = stack.pop()[0]
    answer[time] = len(prices)-time-1

print(answer)

# for i in range(len(prices)):
#     for j in range(i,len(prices)):
#         if i == j:
#             continue
#         else:
#             if prices[i] <= prices[j]:
#                 answer[i] += 1
#             else:
#                 answer[i] += 1
#                 break
# print(answer)