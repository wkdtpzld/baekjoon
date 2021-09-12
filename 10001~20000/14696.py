TC=int(input())

for i in range(TC):
    a_li=list(map(str,input().split()))
    a_li_1=a_li[1:]
    b_li=list(map(str,input().split()))
    b_li_1=b_li[1:]
    if a_li_1.count('4') == b_li_1.count('4'):
        if a_li_1.count('3') > b_li_1.count('3'):
            print('A')
        elif a_li_1.count('3') < b_li_1.count('3'):
            print('B')

        if a_li_1.count('3') == b_li_1.count('3'):
            if a_li_1.count('2') > b_li_1.count('2'):
                print('A')
            elif a_li_1.count('2') < b_li_1.count('2'):
                print('B')

            if a_li_1.count('2') == b_li_1.count('2'):
                if a_li_1.count('1') > b_li_1.count('1'):
                    print('A')
                elif a_li_1.count('1') < b_li_1.count('1'):
                    print('B')

                if a_li_1.count('1') == b_li_1.count('1'):
                    print('D')
    elif a_li_1.count('4') > b_li_1.count('4'):
        print('A')
    elif a_li_1.count('4') < b_li_1.count('4'):
        print('B')
