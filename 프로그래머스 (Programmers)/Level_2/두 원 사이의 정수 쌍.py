from math import sqrt,ceil
def solution(r1, r2):
    answer=0
    for h in range(1,r2+1):
        w1=sqrt(pow(r1,2)-pow(h,2)) if pow(r1,2)-pow(h,2)>=0 else 0
        w2=sqrt(pow(r2,2)-pow(h,2)) if pow(r2,2)-pow(h,2)>=0 else 0
        answer+=4*(int(w2)-ceil(w1)+1)
    return answer