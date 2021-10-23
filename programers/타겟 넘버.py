numbers=[3,2,1,2,3]
target = 6

def soultion(numbers, target):

    size = len(numbers)
    n = (sum(numbers) - target) // 2

    def dfs(target, idx, cnt):
        for i in range(idx,size):
            temp = target
            temp -= numbers[i]
            if temp == 0:
                cnt += 1
            elif temp > 0:
                cnt += dfs(temp, i+1, 0)
            elif temp < 0:
                continue
        return cnt

    return dfs(n,0,0)

print(soultion(numbers, target))