import sys
n,m=map(int,input().split())
n_li=[sys.stdin.readline() for i in range(n)]
m_li=[sys.stdin.readline() for j in range(m)]

result = sorted(list(set(n_li) & set(m_li)))
print(len(result))
for x in result:
    sys.stdout.write(str(x))