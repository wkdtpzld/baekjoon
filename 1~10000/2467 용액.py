import sys

n = int(input())

s = list(map(int,input().split()))
start = 0
end = len(s) - 1
answer = [[0,0]]

c = sys.maxsize

while start < end:
    _sum = s[start] + s[end]

    if abs(_sum) <= c:
        answer.pop()
        answer.append([s[start],s[end]])
        c = abs(_sum)

    if _sum > 0 :
        end -= 1
    elif _sum < 0:
        start += 1
    else:
        break

print(answer[0][0],answer[0][1])