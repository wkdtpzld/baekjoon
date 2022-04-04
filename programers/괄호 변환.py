p="()))((()"

stack=[]
error=[]
for i in range(len(p)):
    if p[i] == "(":
        stack.append(p[i])
    elif p[i] == ")":
        if stack[-1] == "(":
            stack.append(p[i])
        else:
            error.append(p[i])