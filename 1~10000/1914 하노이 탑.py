import sys
input=sys.stdin.readline

n = int(input())

result = []

def hanoi(n,from_hanoi,to_hanoi,aux_hanoi):

    if n == 1:
        result.append([from_hanoi,to_hanoi])
        return
    hanoi(n-1, from_hanoi,aux_hanoi,to_hanoi)
    result.append([from_hanoi,to_hanoi])
    hanoi(n-1,aux_hanoi,to_hanoi,from_hanoi)


if n > 20:
    print(2**n-1)
else:
    hanoi(n, 1, 3, 2)
    print(len(result))
    for i,j in result:
        sys.stdout.write(str(i)+" "+str(j)+'\n')