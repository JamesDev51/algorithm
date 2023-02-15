def solution(number, k):
    stack=[]
    idx=0
    while idx<len(number):
        while k and stack and int(stack[-1])<int(number[idx]):stack.pop();k-=1
        stack.append(number[idx])
        idx+=1
    answer = ''.join(stack)
    if k:
        answer=answer[:-k]
    
    return answer