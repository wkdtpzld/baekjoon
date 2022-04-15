from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

bridge = 0
wait = deque(truck_weights)
crossing = deque([0] * bridge_length)

cnt = 0

while wait or bridge > 0:
    cnt += 1
    bridge -= crossing.popleft()

    if wait and bridge + wait[0] <= weight:
        new_weight = wait.popleft()

        bridge += new_weight
        crossing.append(new_weight)

    else:
        crossing.append(0)

print(cnt)

# 틀림.
#def solution(bridge_length, weight, truck_weights):
# cnt = 1
# stack=[]
#
# for i in truck_weights:
#     if sum(stack) + i > weight:
#         stack.pop(0)
#         stack.append(i)
#         cnt += 1
#     elif sum(stack) + i <= weight:
#         if len(stack) > bridge_length - 1:
#             cnt += bridge_length - 1
#             stack.pop(0)
#             stack.append(i)
#         else:
#             if len(stack) == 0:
#                 stack.append(i)
#                 cnt += bridge_length
#             else:
#                 cnt += 1
#                 stack.append(i)
#
# return cnt