def solution(elements):
    answer = set()
    size=len(elements)
    
    elements=elements+elements

    for i in range(1,size+1):
        lt,rt=0,i
        sub_sum=sum(elements[lt:rt])
        while rt<len(elements):
            answer.add(sub_sum)
            sub_sum-=elements[lt];lt+=1
            sub_sum+=elements[rt];rt+=1
            
    return len(answer)