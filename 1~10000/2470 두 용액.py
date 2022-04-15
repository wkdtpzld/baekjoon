import sys

n = int(input())
s = list(map(int,input().split()))
s.sort()

start = 0
end = len(s) - 1
answer = [[0,0]]

c = sys.maxsize

while start < end:
    _sum = s[start] + s[end]

    if abs(_sum) <= c:
        c = abs(_sum)
        answer.pop()
        answer.append([s[start],s[end]])

    if _sum > 0:
        end -= 1
    elif _sum < 0:
        start += 1
    elif _sum == 0:
        break

print(answer[0][0],answer[0][1])