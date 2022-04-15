import  math

# progresses=[93,30,55]
# speeds=[1,30,5]
#
# answer=[]
# stack=[]
#
# t = math.ceil((100-progresses[0])/speeds[0])
# cnt = 1
# for i in range(1,len(speeds)):
#     if t >= math.ceil((100-progresses[i])/speeds[i]):
#         cnt += 1
#     else:
#         answer.append(cnt)
#         cnt = 1
#         t = math.ceil((100-progresses[i])/speeds[i])
#
# answer.append(cnt)
# print(answer)




def solution(progresses, speeds):
    answer = []
    stack=[]

    for i in range(len(speeds)):
        n =math.ceil(float(100-progresses[i])/speeds[i])
        stack.append(n)

    cnt = 1
    max_arr=stack[0]
    for i in range(1,len(speeds)):
        if max_arr >= stack[i]:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_arr = stack[i]

    answer.append(cnt)
