import heapq

scoville = [1, 1]
K = 7

def solution(scoville, K):
    answer = 0

    scoville.sort()

    heap = []

    for i in scoville:
        heapq.heappush(heap,i)



    while heap[0] < K:
        if heap[0] < K:
            try:
                a = heapq.heappop(heap)
                b = heapq.heappop(heap)

                heapq.heappush(heap,a+(b*2))
                answer += 1
            except IndexError:
                return -1


    return answer

print(solution(scoville,K))