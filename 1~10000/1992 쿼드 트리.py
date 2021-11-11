def quad_tree(x,y,n):
    if(n==1):
        return str(s[x][y])

    next_n = n // 2

    result = []

    flag = s[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if flag != s[i][j]:
                result.extend("(")
                result.extend(quad_tree(x,y,next_n))
                result.extend(quad_tree(x,y+next_n,next_n))
                result.extend(quad_tree(x+next_n,y,next_n))
                result.extend(quad_tree(x+next_n,y+next_n,next_n))
                result.extend(")")

                return result

    return str(s[x][y])

n = int(input())

s=[list(map(int,input())) for i in range(n)]


print(''.join(quad_tree(0,0,n)))
