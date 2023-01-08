def solution(age):
    answer = ''
    while age:
        num=age%10
        answer=chr(num+97)+answer
        
        age//=10
    return answer