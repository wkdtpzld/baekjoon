import heapq

operations = ["I 16","D 1"]

def solution(operations):

    plus_h = []
    minus_h = []

    for i in operations:
        a,b = i.split()
        b = int(b)
        if a == "I":
            heapq.heappush(plus_h,-b)
            heapq.heappush(minus_h,b)
        elif a == "D":
            if b == 1 and len(plus_h) > 0:
                minus_h.remove(-heapq.heappop(plus_h))
            elif b == -1 and len(plus_h) > 0:
                plus_h.remove(-heapq.heappop(minus_h))


    if len(minus_h) == 0:
        answer = [0,0]
    else:
        answer = [-plus_h[0],minus_h[0]]

    return answer


print(solution(operations))