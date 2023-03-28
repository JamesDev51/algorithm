from collections import deque
def go(storey):
    que=deque()
    ret=1e10
    used=dict();used[storey]=0
    que.append((storey,0))
    while que:
        num,cnt=que.popleft()
        if num<0 or 1e8<num:continue
        if num==0:
            ret=min(ret,cnt)
            continue
        
        e=8
        while num%pow(10,e)!=0:e-=1
        
        val=num%pow(10,e+1)
        add_cnt=val//pow(10,e)
        lower_num=num-val
        lower_cnt=val//pow(10,e)
        
        upper_num=num+(pow(10,e+1)-val)
        upper_cnt=10-lower_cnt
        

        if lower_num not in used or cnt+lower_cnt<used[lower_num]:
            used[lower_num]=cnt+lower_cnt
            que.append((lower_num,cnt+lower_cnt))
        if upper_num not in used or cnt+upper_cnt<used[upper_num]:
            used[upper_num]=cnt+upper_cnt
            que.append((upper_num,cnt+upper_cnt))
    return ret
    
def solution(storey):
    answer=go(storey)
    return answer