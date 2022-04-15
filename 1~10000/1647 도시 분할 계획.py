n,m=map(int,input().split())

city=[]

for i in range(m):
    s = list(map(int,input().split()))
    city.append(s)

city.sort(key= lambda x: x[2])
print(city)
connect = set([city[0][0]])

answer = 0

while len(connect) != n:
    for cost in city:
        if cost[0] in connect and cost[1] in connect:
            continue
        else:
        # elif cost[0] in connect or cost[1] in connect:
            connect.update([cost[0],cost[1]])
            answer += cost[2]
            print(connect,answer)
            break

print(answer)