def has369(num):
    ret=0
    while num:
        a=num%10
        if a in [3,6,9]:ret+=1
        num//=10
    return ret

def solution(order):
    answer=has369(order)
        
    return answer