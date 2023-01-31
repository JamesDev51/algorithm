def init(s):
    ret=list()
    for i in range(len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            ret.append(s[i].lower()+s[i+1].lower())
    return ret

def solution(str1, str2):
    answer = 0
    str1_list=init(str1)
    str2_list=init(str2)
    
    if not str1_list and not str2_list:answer=1 #아예 없는 경우 1
    else:
        kinds=set(str1_list).union(set(str2_list))
        str1_hash=dict(); str2_hash=dict()
        for word in kinds: str1_hash[word]=0;str2_hash[word]=0
        for word in str1_list: str1_hash[word]+=1
        for word in str2_list: str2_hash[word]+=1
        total=list(); intersect=list()
        for word in kinds:
            total.extend([word]*max(str1_hash[word],str2_hash[word]))
            intersect.extend([word]*min(str1_hash[word],str2_hash[word]))
        answer=len(intersect)/len(total)
        
    return int(answer*65536)