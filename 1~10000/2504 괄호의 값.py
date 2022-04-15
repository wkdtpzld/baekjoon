li=list(input())


cnt = 0
def check(s):
    stack = []
    flag = True

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        else:
            if i == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    flag = False

            else:
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    flag = False
    if not stack and flag:
        return True
    return False

def sum_check(s):
    stack = []
    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        else:
            if i == ")":
                if stack[-1] == "(":
                    stack[-1] = 2
                else:
                    temp = 0
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j] == "(":
                            stack[-1] = temp * 2
                            break
                        else:
                            temp += stack[-1]
                            stack.pop()
            elif i == "]":
                if stack[-1] == "[":
                    stack[-1] = 3
                else:
                    temp = 0
                    for j in range(len(stack)-1,-1,-1):
                        if stack[j] == "[":
                            stack[-1] = temp * 3
                            break
                        else:
                            temp += stack[-1]
                            stack.pop()
    return sum(stack)

if check(li):
    print(sum_check(li))
else:
    print(0)