pole=[64]
result=int(input())
while sum(pole) > result:
    temp = pole.pop()//2
    pole.extend([temp,temp])
    if sum(pole[:-1]) >= result:
        pole.pop()
print(len(pole))
