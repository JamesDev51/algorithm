user_id_ch=dict()
banned_user_dict=dict()
banned_cnt_dict=dict()
case_set=set()

def pre_process(user_id_list,banned_id_list):
    for banned_id in banned_id_list:
        banned_user_dict[banned_id]=list()
        
        if banned_id not in banned_cnt_dict:banned_cnt_dict[banned_id]=1
        else:banned_cnt_dict[banned_id]+=1
        
        for user_id in user_id_list:
            if len(banned_id)!=len(user_id):continue
            flag=True
            for i in range(len(banned_id)):
                if banned_id[i]=='*':continue
                elif banned_id[i]!=user_id[i]:flag=False;break
            if flag:banned_user_dict[banned_id].append(user_id)
    for user_id in user_id_list:
        user_id_ch[user_id]=0

def dfs(user_id_list,banned_id_list,banned_id_idx):
    global user_id_ch, answer
    if len(banned_id_list)==banned_id_idx:
        user_id_checked=list()
        for user_id in user_id_list:
            if user_id_ch[user_id]:user_id_checked.append(user_id)
        user_id_checked_tuple=tuple(user_id_checked)
        if user_id_checked_tuple not in case_set:
            case_set.add(user_id_checked_tuple)
        return
        
    banned_id=banned_id_list[banned_id_idx]
    for user_id in banned_user_dict[banned_id]:
        if not user_id_ch[user_id]:
            user_id_ch[user_id]=1
            dfs(user_id_list,banned_id_list,banned_id_idx+1)
            user_id_ch[user_id]=0
            
def solution(user_id, banned_id):
    global user_id_ch, answer
    pre_process(user_id, banned_id)
    dfs(user_id, banned_id,0)
    
    return len(case_set)