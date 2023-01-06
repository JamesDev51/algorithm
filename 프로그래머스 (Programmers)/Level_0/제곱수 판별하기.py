def solution(n):
    answer = 2
    for i in range(1,pow(10,3)+1):
        if pow(i,2)==n:answer=1;break
    return answer