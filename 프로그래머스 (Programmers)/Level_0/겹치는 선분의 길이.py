def solution(lines):
    answer = 0
    lineAcc=[0]*(201)
    for line in lines:
        for loc in range(line[0],line[1]):
            if loc<0: lineAcc[abs(loc)+100]+=1
            else:
                lineAcc[loc]+=1
    for i in range(201):
        if lineAcc[i]>=2: answer+=1
    
    
    return answer