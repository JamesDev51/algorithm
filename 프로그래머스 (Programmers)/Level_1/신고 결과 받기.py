def solution(id_list, report, k):
    answer = [0]*len(id_list)
    reported={}
    name_idx={}
    for  i in range(len(id_list)):
        id=id_list[i]
        reported[id]=set()
        name_idx[id]=i
        
    for re in report:
        a,b=re.split(" ")
        reported[b].add(a)
    
    for key,value in reported.items():
        if len(value)>=k:
            for id in value:
                answer[name_idx[id]]+=1
    
    return answer