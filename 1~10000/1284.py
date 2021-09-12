while True:
    n=input()
    if n == "0":
        break
    result=len(n)+1
    for i in n:
        if i == '0':
            result +=4
        elif i == '1':
            result +=2
        else:
            result +=3
    print(result)
