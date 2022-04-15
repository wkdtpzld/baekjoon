def solution(first, last, range):
    if range == 1:
        s[first] = "-"

    else:
        temp = range // 3

        solution(first, first + temp - 1, temp)
        solution(last - temp + 1, last, temp)

while True:
    try:
        n = input()

        if n == "":
            break

        n_s = 3**int(n)

        s = []
        for i in range(n_s):
            s.append(" ")

        solution(0, n_s - 1, n_s)

        result = ""
        for i in s:
            result += i
        print(result)
    except EOFError:
        break
