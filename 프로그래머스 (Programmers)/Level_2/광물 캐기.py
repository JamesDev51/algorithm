answer=1e9
tired_equip_mineral=[[1,1,1],[5,1,1],[25,5,1]]
attr_idx={'diamond':0,'iron':1,'stone':2}
def back_tracking(picks,minerals,idx,pick_idx,used_cnt,tired):
    global answer
    if idx==len(minerals) or (sum(picks)==0 and used_cnt==5):
        answer=min(answer,tired)
    if answer<=tired:return 

    mineral_idx=attr_idx[minerals[idx]]
    if used_cnt<5:
        back_tracking(picks,minerals,idx+1,pick_idx,used_cnt+1,tired+tired_equip_mineral[pick_idx][mineral_idx])
    else:
        for new_pick_idx in range(3):
            if picks[new_pick_idx]>0:
                picks[new_pick_idx]-=1
                back_tracking(picks,minerals,idx+1,new_pick_idx,1,tired+tired_equip_mineral[new_pick_idx][mineral_idx])
                picks[new_pick_idx]+=1
            
    
def solution(picks, minerals):
    global answer
    back_tracking(picks,minerals,0,-1,5,0,)
    return answer