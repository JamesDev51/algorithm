def solution(number, limit, power):
    answer = 0
    d=[1]*100001
    for i in range(2,100001):
        for j in range(i,100001,i):d[j]+=1
    
    for num in range(1,number+1):
        if d[num]>limit:answer+=power
        else:answer+=d[num]
        
    
    return answer