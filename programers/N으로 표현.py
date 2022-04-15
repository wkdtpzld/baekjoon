def solution(N, number) :
    answer = 0

    if N == number :
        return 1

    s = [set() for i in range(8)]

    for i in range(1,9):
        s[i-1].add(int(str(N)*i))

    for i in range(1,8):
        for j in range(i):
            for x in s[j]:
                for y in s[i-j-1]:

                    s[i].add(x+y)
                    s[i].add(x-y)
                    s[i].add(x*y)
                    if y != 0 and x != 0:
                        s[i].add(x//y)

        if number in s[i]:
            answer = i+1
            break

    if answer == 0:
        answer = -1

    return answer

print(solution(5,31168))

