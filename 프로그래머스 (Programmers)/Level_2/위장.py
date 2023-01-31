def solution(clothes):
    answer = 0
    kinds_hash=dict()
    for _,kind in clothes:
        if kind not in kinds_hash:kinds_hash[kind]=1
        else: kinds_hash[kind]+=1
    
    answer=1
    for value in kinds_hash.values():
        answer*=(value+1)
    
    return answer-1