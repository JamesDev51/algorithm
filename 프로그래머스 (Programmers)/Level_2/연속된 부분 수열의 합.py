def solution(sequence, k):
    answer = []
    lt,rt=0,0
    length=float('inf')
    for i in range(1,len(sequence)):sequence[i]+=sequence[i-1]
    sequence.insert(0,0)
    
    while rt<len(sequence):
        sub_sum=sequence[rt]-sequence[lt]
        if sub_sum>=k:
            if sub_sum==k and (rt-1-lt)<length:
                length=(rt-1-lt)
                answer=[lt,rt-1]
                
            lt+=1
        else:
            rt+=1
    return answer