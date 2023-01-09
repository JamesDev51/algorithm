def solution(s):
    answer = 0
    splited=s.split(" ")
    last_num=0
    for com in splited:
        if com=="Z":
            answer-=last_num
        else:
            answer+=int(com)
            last_num=int(com)
            
    return answer