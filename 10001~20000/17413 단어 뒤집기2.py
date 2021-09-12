import sys

string=sys.stdin.readline().rstrip()

word = ""
result = ""
flag = True

for i in string:

    if flag == True:
        if i == '<':
            flag = False
            word += i
        elif i == " ":
            word += i
            result += word
            word = ""
        else:
            word = i + word

    else:
        word += i
        if i == '>':
            flag = True
            result += word
            word = ""

print(result + word)