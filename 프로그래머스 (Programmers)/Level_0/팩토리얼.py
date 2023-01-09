def solution(n):
    answer = 1
    value=1
    while value<=n:
        answer+=1
        value*=answer
    return answer-1