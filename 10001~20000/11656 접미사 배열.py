word=str(input())
li=[]
for _ in word:
    li.append(word)
    word=word[1:]
for i in sorted(li):
    print(i)
