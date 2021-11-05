participant = ["leo","kiki","eden"]
completion = ["eden","kiki"]


def solution(participant, completion):
    dic = {}

    answer = ''
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    for i in completion:
        dic[i] -= 1

    for key, values in enumerate(dic):
        if dic[values] > 0:
            answer += values


    return answer

print(solution(participant,completion))
