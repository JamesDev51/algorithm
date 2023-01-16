def solution(d, budget):
    answer = 0
    d.sort()
    idx=0
    while idx<len(d) and d[idx]<=budget:
        budget-=d[idx]
        idx+=1
        answer+=1
    return answer