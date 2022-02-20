s1=list(input())
s2=list(input())

s = [[0]*(len(s2)+1) for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            s[i][j] = s[i-1][j-1] + 1
        else:
            s[i][j] = max(s[i-1][j],s[i][j-1])

print(s[-1][-1])