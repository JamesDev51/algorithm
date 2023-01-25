def solution(s):

    stack=[]
    for ch in s:
        if not stack: stack.append(ch)
        elif stack and stack[-1]==ch:stack.pop()
        else: stack.append(ch)
    
    answer = 1 if not stack else 0
    return answer