def solution(num, k):
    answer = -1
    idx=1
    while num:
        a=num%10
        if a==k:
            answer=idx
        num//=10
        idx+=1
        
    return idx-answer if answer!=-1 else -1