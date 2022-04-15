n = int(input())
m = int(input())

costs = []

for i in range(m):
    s = list(map(int,input().split()))
    costs.append(s)

costs.sort(key= lambda x : x[2])

network = set([costs[0][0]])
result = 0

while len(network) != n:
    for cost in costs:
        if cost[1] in network and cost[0] in network:
            continue
        elif cost[1] in network or cost[0] in network:
            network.update([cost[1],cost[0]])
            result += cost[2]
            break

print(result)