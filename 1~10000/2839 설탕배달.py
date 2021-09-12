s=0
while True:
    o,m=map(int,input().split())
    s += 1
    if o == 0 and m == 0:
        break
    while True:
        E,F=map(str,input().split())
        if E == 'F':
            if m <= 0:
                continue
            m += int(F)

        elif E == 'E':
            if m <= 0:
                continue
            m -= int(F)

        elif E == '#' and F == '0':
            if m<o*2 and m>o/2:
                print(s,':-)')
                break
            elif m <= 0:
                print(s, 'RIP')
                break
            else:
                print(s,':-(')
                break