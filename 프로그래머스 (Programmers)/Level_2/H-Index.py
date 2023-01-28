def solution(citations):
    answer=0
    citations.sort(reverse=True)
    size=len(citations)
    for i in range(1,size+1):
        if citations[i-1]>=i:answer=i
        else:break
    return answer