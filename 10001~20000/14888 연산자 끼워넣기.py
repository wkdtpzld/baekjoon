n = int(input())
s = list(map(int,input().split()))
arr=list(map(int,input().split()))

max_result=-100000001
min_result= 100000001

def solution(cnt,result,p,m,multy,div):
    global max_result
    global min_result

    if cnt == n:
        max_result = max(max_result,result)
        min_result = min(min_result,result)
        return
    else:
        if p:
            solution(cnt + 1 , result + s[cnt], p-1,m,multy,div)
        if m:
            solution(cnt + 1 , result - s[cnt], p,m-1,multy,div)
        if multy:
            solution(cnt + 1 , result * s[cnt], p,m,multy-1,div)
        if div:
            solution(cnt + 1 , int(result/s[cnt]), p,m,multy,div-1)


solution(1,s[0],arr[0],arr[1],arr[2],arr[3])

print(max_result)
print(min_result)

