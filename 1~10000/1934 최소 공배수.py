TC=int(input())
for _ in range(TC):
    a,b=map(int,input().split())
    a_1,b_1=a,b
    while b  > 0:
        a,b = b, a % b

    print(int(a_1 * b_1 / a))