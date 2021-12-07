priorities = [2,1,3,2]
location = 2

def solution(priorities, location):
    answer = 0

    cnt = 0

    v = [i for i in range(len(priorities))]
    v[location] = "ans"


    s = []

    while priorities:
        if priorities[0] == max(priorities):
            if v[0] == "ans":

                return answer + 1
            else:
                answer += 1
                v.pop(0)

                priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            v.append(v.pop(0))



print(solution(priorities, location))