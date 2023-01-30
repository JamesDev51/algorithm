dic=dict()
def init():
    for i in range(65,65+26):
        dic[chr(i)]=i-64

def solution(msg):
    answer = []
    init()
    
    dic_new_idx=27
    idx=0
    while idx<len(msg):
        w=msg[idx]
        while idx+1<len(msg) and w+msg[idx+1] in dic:
            w+=msg[idx+1]
            idx+=1
        answer.append(dic[w])
        if idx+1<len(msg):
            dic[w+msg[idx+1]]=dic_new_idx
            dic_new_idx+=1
        idx+=1    
    return answer