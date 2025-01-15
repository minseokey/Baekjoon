def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if len(phone_book[i]) < len(phone_book[j]) and phone_book[i][0] == phone_book[j][0]:
                if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                    return False
            else:
                break
    
    return True
            