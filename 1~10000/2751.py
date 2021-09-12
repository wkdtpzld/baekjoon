def insertionSort(x):
    for end in range(1, len(x)):
        for i in range(end, 0 ,-1):
            if x[i-1] > x[i]:
                x[i-1],x[i] = x[i],x[i-1]
n=int(input())
x=[]
for _ in range(n):
    x.append(int(input()))

insertionSort(x)
print(x)