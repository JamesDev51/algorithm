def solution(s):
    answer = True
    
    stack=[]
    for ch in s:
        if ch == "(":stack.append(ch)
        elif ch==")" and stack: stack.pop()
        else: answer=False;break
    answer=answer if not stack else False
    return answer