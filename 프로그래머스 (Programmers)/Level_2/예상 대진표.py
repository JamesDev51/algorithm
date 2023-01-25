def solution(n,a,b):
    answer = 1
    small=min(a,b); big=max(a,b)
    
    while (small+1)//2 != (big+1)//2:
        if small%2==0:small//=2
        else: small=(small+1)//2
        
        if big%2==0:big//=2
        else: big=(big+1)//2
        answer+=1
        

    return answer