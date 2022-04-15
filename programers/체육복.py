n = 9
lost = [1,2,4]
reserve = [1,3]

def solution(n, lost, reserve):

    set_r = set(reserve) - set(lost)

    set_l = set(lost) - set(reserve)


    for i in set_r:
        if i-1 in set_l:
            set_l.remove(i-1)
        elif i+1 in set_l:
            set_l.remove(i+1)

    return n - len(set_l)

print(solution(n,lost,reserve))