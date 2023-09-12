def solution(name):
    def find_a_list():
        a_list=[]
        idx=0
        while idx<n:
            if name[idx]=='A':
                start_idx=idx
                idx+=1
                while idx<n and name[idx]=='A':idx+=1
                a_list.append([start_idx,idx])
            idx+=1
        return a_list
        
        
    n=len(name)
    updown_cnt=[0]*n
    
    for i in range(n):
        ch=name[i]
        updown_cnt[i]=min(ord(ch)-ord('A'),ord('Z')-ord(ch)+1)
    updown_cnt_sum=sum(updown_cnt)
    answer = updown_cnt_sum+(n-1)
    
    a_list=find_a_list()
    for start_idx, end_idx in a_list:
        move_cnt=min(max(start_idx-1,0)*2+(n-end_idx),(n-end_idx)*2+max(start_idx-1,0))+updown_cnt_sum
        answer=min(answer,move_cnt)
    return answer