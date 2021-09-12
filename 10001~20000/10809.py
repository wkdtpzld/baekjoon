list_x=[]
for i in range(26):
    list_x.append(-1)
a=list(input())
for index,value in enumerate(a):
    if(list_x[ord(value)-ord('a')]== -1):
        list_x[ord(value) - ord('a')] = index
for i in list_x:
    print(i,end=" ")