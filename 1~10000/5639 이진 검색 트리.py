import sys
sys.setrecursionlimit(10**9)

input=sys.stdin.readline

preorder = []

while True:
    a=(input().rstrip())
    if a == "":
        break
    preorder.append(int(a))



def postorder(start , end):
    if start > end:
        return
    division = end +1

    for i in range(start+1,end + 1):
        if preorder[start] < preorder[i]:
            division = i
            break

    postorder(start+1,division-1)
    postorder(division,end)
    print(preorder[start])

postorder(0,len(preorder)-1)

