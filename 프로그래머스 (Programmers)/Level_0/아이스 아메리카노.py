def solution(money):
    answer = [0,0]
    answer[0]=money//5500
    answer[1]=money-answer[0]*5500
    return answer