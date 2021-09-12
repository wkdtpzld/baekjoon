while True:
    a=list(map(str,input().lower().split()))
    if a[0] == '*':
        break

    cnt=0
    for i in range(len(a)):
        if i != len(a)-1:
            if a[i][0] == a[i+1][0]:
                pass
            else:
                print('N')
                break
        else:
            print('Y')