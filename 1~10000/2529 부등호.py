n=int(input())
string=list(map(str,input().split()))
nums=[0]*10

min_value=""
max_value=""

def check(i,j,k):
    if k == '<':
        return i < j
    else:
        return j < i


def solve(idx,s):
    global min_value, max_value

    if (idx == n+1):
        if len(min_value) == 0:
            min_value = s
        else:
            max_value = s
        return
    for i in range(10):
        if nums[i] == 0:
            if idx == 0 or check(s[-1],str(i),string[idx-1]):
                nums[i] = 1
                solve(idx+1,s+str(i))
                nums[i] = 0

solve(0,"")
print(max_value)
print(min_value)
