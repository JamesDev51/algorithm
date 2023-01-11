def solution(n):
    answer = -1
    sqr=1
    while pow(sqr,2)<=n:
        if pow(sqr,2)==n:
            answer=pow(sqr+1,2)
            break
        sqr+=1
    return answer