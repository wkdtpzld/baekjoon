import copy
a=list(map(int,input().split(" "))) # [8.7.6.5.4.3.2.1]
b=a.copy() # [8.7.6.5.4.3.2.1]
b.sort() #[1.2.3.4.5.6.7.8]
if a == b:
    print("ascending")
elif a == list(reversed(b)):
    print("descending")
else:
    print("mixed")
