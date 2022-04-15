# n = int(input())
# s = [list(map(int,input().split())) for i in range(n)]
# stack = []
# move=list(map(int,input().split()))
# cnt = 0
#
# while move:
#     a = move[0]-1
#
#     del move[0]
#
#     for i in range(n):
#         if s[i][a] == 0:
#             continue
#         else:
#             if len(stack) == 0:
#                 stack.append(s[i][a])
#                 s[i][a] = 0
#             else:
#                 if stack[-1] == s[i][a]:
#                     stack.pop()
#                     cnt += 2
#                 else:
#                     stack.append(s[i][a])
#                 s[i][a] = 0
#                 break
# print(cnt)
#
#

board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
def solution(board, moves):
    answer = 0
    stack = []

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] == 0:
                pass
            else:
                stack.append(board[j][i-1])
                board[j][i-1] = 0

                if len(stack) > 1:
                    if stack[-1] == stack[-2]:
                        stack.pop()
                        stack.pop()
                        answer +=2
                break
    return answer
print(solution(board,moves))

