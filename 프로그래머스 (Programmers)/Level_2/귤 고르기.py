def solution(k, tangerine):
    answer = 0
    tang_hash=dict()
    for tang in tangerine:
        if tang not in tang_hash: tang_hash[tang]=1
        else: tang_hash[tang]+=1
    tang_items=list(tang_hash.items())
    tang_items.sort(key=lambda x:-x[1])
    total=0
    for _,count in tang_items:
        total+=count;answer+=1
        if total>=k:break
        
    return answer