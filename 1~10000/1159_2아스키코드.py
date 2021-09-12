TC=int(input())
a_li=[0 for i in range(26)]
for i in range(TC):
    a=input()
    a_li[ord(a[0])-ord('a')]+=1
for i in range(len(a_li)):
    if a_li[i] >= 5:
        print(chr(ord('a')+i),end="")