def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x:len(x))
    phone_hash=set()
    for phone in phone_book:
        length=len(phone)
        for i in range(length):
            if phone[:i] in phone_hash:answer=False
        phone_hash.add(phone)
        if not answer:break
    
    return answer