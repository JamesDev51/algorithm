def solution(my_string):
    answer=0
    tmpNum=0
    for s in my_string:
        if s.isdigit():
            tmpNum*=10
            tmpNum+=int(s)
        else:
            answer+=tmpNum
            tmpNum=0
    answer+=tmpNum
    return answer