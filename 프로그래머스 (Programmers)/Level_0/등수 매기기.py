

def solution(score):
    answer = [0]*(len(score))
    avgs=[0]*len(score)
    for idx,item in enumerate(score):
        eng,math=item
        avgs[idx]=(float(eng+math)/2,idx)
    avgs.sort(reverse=True)
    largest=101
    ranking=0
    acc=0

    for score,idx in avgs:
        if score<largest:
            ranking+=(1+acc)
            acc=0
            largest=score
        elif score==largest:
            acc+=1
        answer[idx]=ranking
    
    return answer