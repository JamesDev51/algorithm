def solution(N, stages):
    answer = []
    fail_rates=[0]*(N+1)
    stages_count=[0]*(N+1)
    for stage in stages: 
        if stage<=N:stages_count[stage]+=1
    total_stages_count=len(stages)
    for i in range(1,N+1):
        if total_stages_count==0:continue
        fail_rates[i]=stages_count[i]/total_stages_count
        total_stages_count-=stages_count[i]
    tmp_answer=list(enumerate(fail_rates))
    tmp_answer.sort(key=lambda x :(-x[1],x[0]))
    for idx,_ in tmp_answer: 
        if idx==0:continue
        answer.append(idx)
        
    
    return answer