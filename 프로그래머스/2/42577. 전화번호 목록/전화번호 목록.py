def solution(phone_book):
    p = {}
    for num in phone_book:
        p[num] = True
    for num in phone_book:
        piece = ''
        for i in num[:-1]:
            piece += i
            if piece in p:
                answer = False
                return answer
    
    answer = True
    return answer

