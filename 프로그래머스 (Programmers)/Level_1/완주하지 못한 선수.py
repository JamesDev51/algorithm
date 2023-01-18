part_hash=dict()

def solution(participant, completion):
    answer=''
    for part in participant:
        if part not in part_hash: part_hash[part]=1
        else: part_hash[part]+=1
    for comp in completion:
        part_hash[comp]-=1
    for key,value in part_hash.items():
        if value>0:answer=key;break
        
    return answer