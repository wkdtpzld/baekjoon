n,m = map(int,input().split())

s = list(map(str,input().split()))
s.sort()

def dfs(a):

    if len(li) == n:
        cnt = 0
        cnt_v = 0
        for i in range(n):
            if li[i] in 'aeiou':
                cnt += 1
            else:
                cnt_v += 1

        if cnt >= 1 and cnt_v >= 2:
            x = ''.join(map(str,li))
            print(x)
        return
    for i in range(a,m):
        if s[i] not in li:
            try:
                if ord(s[i]) > ord(li[-1]):
                    li.append(s[i])
                    dfs(a)
                    li.pop()
            except IndexError:
                li.append(s[i])

for i in range(m):
    li=[]
    dfs(i)

# dic={}
# p = ['a','e','i','o','u']
# cons = [x for x in s if x not in p]
