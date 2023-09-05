def solution(n, k, enemy):
    answer = k
    if sum(enemy)<=n or len(enemy)<=k:
        return len(enemy)
        
    lt,rt=k,len(enemy)
    while lt<=rt:
        mid=(lt+rt)//2
        sorted_enemy=sorted(enemy[:mid])
        if sum(sorted_enemy[:mid-k])<=n:
            answer=max(answer,mid)
            lt=mid+1
            
        else:
            rt=mid-1
        
        
    return answer