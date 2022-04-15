import sys
input = sys.stdin.readline
n,m = map(int,input().split())
li = []
for i in range(n):
    li.append(int(input()))

li.sort()
answer = 0

def binary_search(start,end,arr):
    global answer

    while start <= end:

        cnt = 1
        mid = (start + end) // 2
        current = arr[0]

        for i in range(1,n):
            if arr[i] >= current + mid:
                cnt += 1
                current = arr[i]

        if cnt >= m:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1


start = 0
end = li[-1] - li[0]
binary_search(start,end,li)

print(answer)