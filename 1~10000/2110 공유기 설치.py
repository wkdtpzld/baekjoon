a,b=map(int,input().split())
li=[int(input()) for _ in range(a)]
li.sort()

def binary_search(array,start,end):

    while start <= end:
        mid = (start + end ) // 2
        current = array[0]
        cnt = 1

        for i in range(1,len(array)):
            if array[i] >= current + mid:
                cnt += 1
                current = array[i]

        if cnt >= b:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

answer = 0
start = 1
end = li[-1] - li[0]

binary_search(li,start,end)
print(answer)