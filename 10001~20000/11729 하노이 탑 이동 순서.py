n = int(input())

def hanoi(n,from_hanoi,to_hanoi,aux_hanoi):
    if n == 1:
        print(from_hanoi,to_hanoi)
        return
    hanoi(n-1,from_hanoi,aux_hanoi,to_hanoi)
    print(from_hanoi,to_hanoi)
    hanoi(n-1,aux_hanoi,to_hanoi,from_hanoi)

s = 2**n - 1
print(s)
hanoi(n,1,3,2)