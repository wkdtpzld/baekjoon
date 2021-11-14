n =  int(input())

def soulution(n):
    if n < 1:
        return "0"

    elif n == 1:
        return "1"

    elif n % 2 == 1:

        return soulution(int(n//2))+"1"
    elif n % 2 == 0:

        return soulution(int(n//2))+"0"

a= soulution(n)
print(a)
