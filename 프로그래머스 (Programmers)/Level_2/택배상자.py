def solution(order):
    answer=0
    stack=list()
    
    now_idx=0
    for box in range(1,max(order)+1):
        while stack and stack[-1]==order[now_idx]:
            stack.pop()
            now_idx+=1
            answer+=1
        if box==order[now_idx]:
            answer+=1
            now_idx+=1
        else:
            stack.append(box)
    while stack and stack[-1]==order[now_idx] and now_idx<len(order):
        stack.pop()
        now_idx+=1
        answer+=1
    return answer