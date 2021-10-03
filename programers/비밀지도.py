def solution(n, arr1, arr2):
    answer = []
    result = [[0] * n for i in range(n)]
    temp = []
    for i in range(1, n + 1):
        temp.append(2 ** (n - i))

    for i in range(n):
        while arr1[i] != 0:
            for j in range(n):
                if arr1[i] >= temp[j]:
                    arr1[i] -= temp[j]
                    result[i][j] = 1

    for i in range(n):
        while arr2[i] != 0:
            for j in range(n):
                if arr2[i] >= temp[j]:
                    arr2[i] -= temp[j]
                    result[i][j] = 1
    a = ""
    for i in result:
        for j in i:
            if j == 1:
                a += '#'
            else:
                a += " "
        answer.append(a)
        a = ""
    return answer
