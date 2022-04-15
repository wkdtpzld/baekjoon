people = [70,50,80,50,30]
limit = 100

def solution(people, limit):

    people.sort(reverse=True)
    start , end = 0 , len(people) - 1
    cnt = len(people)

    while start < end:

        if people[start] + people[end] <= limit:
            end -= 1
            cnt -= 1
        start += 1

    return cnt


print(solution(people,limit))