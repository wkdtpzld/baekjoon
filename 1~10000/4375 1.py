while True:
    try:
        n=int(input())
        i=1
        arr=10
        while i % n != 0:
            if i % n !=0:
                i += arr
                arr *= 10
        i_s=str(i)
        print(len(i_s))
    except EOFError:
        break