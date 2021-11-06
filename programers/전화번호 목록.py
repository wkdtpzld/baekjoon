phone_book = ["12","123","1235","567","88"]



def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):

        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
        else:
            continue

    return answer

print(solution(phone_book))
print(phone_book)