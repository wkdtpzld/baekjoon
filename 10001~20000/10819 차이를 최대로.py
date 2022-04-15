n=int(input())
s=list(map(int,input().split()))

arr=[]
result=0

def dfs():
    global result
    if len(arr) == n:
        sum_arr = 0
        for i in range(n-1):
            sum_arr += abs(s[arr[i]]-s[arr[i+1]])
        result = max(result,sum_arr)

    for i in range(len(s)):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()

print(result)