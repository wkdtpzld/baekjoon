import sys

input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

# s = [[0]*(len(s2)+1) for i in range(len(s1)+1)]

prev = [0]*(len(s2)+1)
answer = 0

for i in range(len(s1)):
    cur = [0] * (len(s2)+1)
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            cur[j+1] = prev[j] + 1

    answer = max(answer,max(cur))
    prev = cur[:]

print(answer)