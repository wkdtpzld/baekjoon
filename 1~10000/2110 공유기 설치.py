a,b=map(int,input().split())
li=[int(input()) for _ in range(a)]
li.sort()
print(li)
start=1
end=max(li) - min(li)
while True:
    mid = (start + end) //2