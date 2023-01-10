def solution(sides):
    answer = 0
    now_largest=max(sides)
    now_shortest=min(sides)
    for left_line in range(1,now_largest+1):
        if left_line+now_shortest>now_largest:answer+=1
    for i in range(now_largest+1,now_shortest+now_largest):answer+=1
        
        
    return answer