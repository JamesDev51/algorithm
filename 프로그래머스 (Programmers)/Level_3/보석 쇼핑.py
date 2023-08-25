from collections import deque
def solution(gems):
    answer = []
    n=len(gems)
    gems_set_size=len(set(gems))
    
    lt,rt=gems_set_size,n
    while lt<=rt:
        mid=(lt+rt)//2
        move_set=set()
        move_hash=dict()
        for i in range(mid):
            gem=gems[i]
            gem=gems[i]
            if gem not in move_hash:move_hash[gem]=1
            else:move_hash[gem]+=1
            move_set.add(gem)
            
        flag=False
        if len(move_set)==gems_set_size:
            answer=[1,mid]
            flag=True
        else:
            for i in range(mid,n):
                out_gem=gems[i-mid]
                move_hash[out_gem]-=1
                if move_hash[out_gem]==0:move_set.remove(out_gem)
            
                in_gem=gems[i]
                if in_gem not in move_hash:move_hash[in_gem]=1
                else:move_hash[in_gem]+=1
                move_set.add(in_gem)

                if len(move_set)==gems_set_size:answer=[i-mid+2,i+1];flag=True;break
        if len(answer)==gems_set_size:break
        if not flag:lt=mid+1
        else:rt=mid-1
    return answer